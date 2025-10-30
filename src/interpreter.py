#!/usr/bin/env python3
"""
🐯 TigerByte Interpreter v0.1
A minimal starter interpreter for TigerByte source files (.tb)
-------------------------------------------------------------
This script reads TigerByte source files, validates them,
and executes simple TigerByte commands.

Author: Rangala Raj Kumar
Date: 27 October 2025
License: MIT
"""


from .banners import display_random_banner, display_banner_by_name
from debug import Debugger
from config import VERSION, REPO_URL
import sys
import os
import argparse

# Token Types
TT_INT, TT_ID, TT_ASSIGN, TT_PLUS, TT_MINUS, TT_PRINT, TT_EOF, TT_STRING = (
    'INT', 'ID', 'ASSIGN', 'PLUS', 'MINUS', 'PRINT', 'EOF', 'STRING'
)
TT_IF, TT_THEN, TT_ELSE = 'IF', 'THEN', 'ELSE'
TT_EQ, TT_NEQ, TT_LT, TT_GT, TT_LTE, TT_GTE = 'EQ', 'NEQ', 'LT', 'GT', 'LTE', 'GTE'
TT_LPAREN, TT_RPAREN = 'LPAREN', 'RPAREN'

class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value
    def __repr__(self):
        return f"Token({self.type}, {self.value!r})"

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None

    def advance(self):
        self.pos += 1
        if self.pos >= len(self.text):
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def peek(self):
        nxt = self.pos + 1
        if nxt >= len(self.text):
            return None
        return self.text[nxt]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def skip_comment(self):
        # comments start with # to end of line
        while self.current_char is not None and self.current_char != '\n':
            self.advance()

    def integer(self):
        s = ''
        while self.current_char is not None and self.current_char.isdigit():
            s += self.current_char
            self.advance()
        return int(s)

    def _id(self):
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        low = result.lower()
        if low == 'print':
            return Token(TT_PRINT, 'print')
        if low == 'if':
            return Token(TT_IF, 'if')
        if low == 'then':
            return Token(TT_THEN, 'then')
        if low == 'else':
            return Token(TT_ELSE, 'else')
        return Token(TT_ID, result)

    def string(self):
        # assumes current_char == " or '
        quote = self.current_char
        self.advance()
        s = ''
        while self.current_char is not None and self.current_char != quote:
            # support escape for \" or \'
            if self.current_char == '\\' and self.peek() == quote:
                self.advance()
                s += self.current_char
                self.advance()
                continue
            s += self.current_char
            self.advance()
        if self.current_char == quote:
            self.advance()
            return Token(TT_STRING, s)
        raise Exception("Unterminated string literal")

    def get_next_token(self):
        while self.current_char is not None:
            # whitespace
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            # comments
            if self.current_char == '#':
                self.skip_comment()
                continue
            # numbers
            if self.current_char.isdigit():
                return Token(TT_INT, self.integer())
            # identifiers / keywords
            if self.current_char.isalpha() or self.current_char == '_':
                return self._id()
            # strings
            if self.current_char in ('"', "'"):
                return self.string()
            # operators and punctuation
            if self.current_char == '=':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token(TT_EQ, '==')
                return Token(TT_ASSIGN, '=')
            if self.current_char == '+':
                self.advance()
                return Token(TT_PLUS, '+')
            if self.current_char == '-':
                self.advance()
                return Token(TT_MINUS, '-')
            if self.current_char == '!':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token(TT_NEQ, '!=')
                raise Exception('Unexpected "!"')
            if self.current_char == '<':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token(TT_LTE, '<=')
                return Token(TT_LT, '<')
            if self.current_char == '>':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return Token(TT_GTE, '>=')
                return Token(TT_GT, '>')
            if self.current_char == '(':
                self.advance()
                return Token(TT_LPAREN, '(')
            if self.current_char == ')':
                self.advance()
                return Token(TT_RPAREN, ')')

            raise Exception(f'Unknown char: {self.current_char}')
        return Token(TT_EOF, None)

# AST Nodes
class AST: pass

class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

class Var(AST):
    def __init__(self, token):
        self.token = token
        self.name = token.value

class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Assign(AST):
    def __init__(self, left, op, right):
        self.left = left  # Var node
        self.op = op
        self.right = right

class Print(AST):
    def __init__(self, expression):
        self.expression = expression

class Compare(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class If(AST):
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch

# Parser
class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self, expected_type=None):
        if expected_type:
            raise Exception(f'Parser Error: Expected {expected_type}, got {self.current_token.type}')
        raise Exception(f'Parser Error: Invalid syntax at {self.current_token}')

    def consume(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(expected_type=token_type)

    def peek_next_token_type(self):
        temp = Lexer(self.lexer.text)
        temp.pos = self.lexer.pos
        temp.current_char = self.lexer.current_char
        return temp.get_next_token().type

    def factor(self):
        token = self.current_token
        if token.type == TT_PLUS:
            self.consume(TT_PLUS)
            node = self.factor()
            return node
        if token.type == TT_MINUS:
            # unary minus
            self.consume(TT_MINUS)
            node = self.factor()
            # represent unary minus as BinOp(0 - node)
            return BinOp(Num(Token(TT_INT, 0)), Token(TT_MINUS, '-'), node)
        if token.type == TT_INT:
            self.consume(TT_INT)
            return Num(token)
        if token.type == TT_ID:
            self.consume(TT_ID)
            return Var(token)
        if token.type == TT_STRING:
            self.consume(TT_STRING)
            # keep strings as plain Python values wrapped in Num-like node for printing convenience
            return token.value
        if token.type == TT_LPAREN:
            self.consume(TT_LPAREN)
            node = self.expr()
            self.consume(TT_RPAREN)
            return node
        self.error()

    def expr(self):
        node = self.factor()
        while self.current_token.type in (TT_PLUS, TT_MINUS):
            op = self.current_token
            if op.type == TT_PLUS:
                self.consume(TT_PLUS)
            elif op.type == TT_MINUS:
                self.consume(TT_MINUS)
            right = self.factor()
            node = BinOp(node, op, right)
        return node

    def comparison(self):
        left = self.expr()
        if self.current_token.type in (TT_EQ, TT_NEQ, TT_LT, TT_GT, TT_LTE, TT_GTE):
            op = self.current_token
            self.consume(op.type)
            right = self.expr()
            return Compare(left, op, right)
        return left

    def command(self):
        token = self.current_token
        # assignment: ID = expr
        if token.type == TT_ID and self.peek_next_token_type() == TT_ASSIGN:
            left = Var(token)
            self.consume(TT_ID)
            op = self.current_token
            self.consume(TT_ASSIGN)
            right = self.expr()
            return Assign(left, op, right)
        # print
        if token.type == TT_PRINT:
            self.consume(TT_PRINT)
            if self.current_token.type == TT_STRING:
                val = self.current_token.value
                self.consume(TT_STRING)
                return Print(val)
            else:
                return Print(self.expr())
        # if-then-else
        if token.type == TT_IF:
            self.consume(TT_IF)
            cond = self.comparison()
            if self.current_token.type == TT_THEN:
                self.consume(TT_THEN)
            else:
                self.error(expected_type=TT_THEN)
            then_cmd = self.command()
            else_cmd = None
            if self.current_token.type == TT_ELSE:
                self.consume(TT_ELSE)
                else_cmd = self.command()
            return If(cond, then_cmd, else_cmd)
        # fallback expression (e.g., standalone arithmetic)
        if token.type in (TT_INT, TT_ID, TT_MINUS, TT_LPAREN):
            return self.expr()
        self.error()

    def parse(self):
        statements = []
        while self.current_token.type != TT_EOF:
            # skip stray newlines handled by lexer as whitespace
            stmt = self.command()
            statements.append(stmt)
        return statements

# Interpreter
class Interpreter:
    def __init__(self):
        self.globals = {}

    def visit(self, node):
        method = 'visit_' + (type(node).__name__ if not isinstance(node, str) else 'Str')
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f'No visit_{type(node).__name__} method')

    def visit_Num(self, node):
        return node.value

    def visit_Str(self, node):
        return node  # raw string

    def visit_Var(self, node):
        name = node.name
        if name in self.globals:
            return self.globals[name]
        raise Exception(f'NameError: {name} is not defined')

    def visit_BinOp(self, node):
        left = self.visit(node.left) if isinstance(node.left, AST) else node.left if not isinstance(node.left, str) else node.left
        right = self.visit(node.right) if isinstance(node.right, AST) else node.right if not isinstance(node.right, str) else node.right
        if node.op.type == TT_PLUS:
            return left + right
        if node.op.type == TT_MINUS:
            return left - right
        raise Exception(f'Unsupported binary operator: {node.op.type}')

    def visit_Assign(self, node):
        name = node.left.name
        value = self.visit(node.right) if isinstance(node.right, AST) else node.right
        self.globals[name] = value
        return None

    def visit_Print(self, node):
        if isinstance(node.expression, AST):
            print(self.visit(node.expression))
        elif isinstance(node.expression, str):
            print(node.expression)
        else:
            # raw number or Python value
            print(node.expression)

    def visit_Compare(self, node):
        left = self.visit(node.left) if isinstance(node.left, AST) else node.left
        right = self.visit(node.right) if isinstance(node.right, AST) else node.right
        t = node.op.type
        if t == TT_EQ:
            return left == right
        if t == TT_NEQ:
            return left != right
        if t == TT_LT:
            return left < right
        if t == TT_GT:
            return left > right
        if t == TT_LTE:
            return left <= right
        if t == TT_GTE:
            return left >= right
        raise Exception('Unknown comparison')

    def visit_If(self, node):
        cond = self.visit(node.condition) if isinstance(node.condition, AST) else node.condition
        if cond:
            return self.visit(node.then_branch)
        if node.else_branch is not None:
            return self.visit(node.else_branch)
        return None

def run_tigerbyte_file(filepath: str, debug_enabled: bool = False):
    if not filepath.endswith(".tb"):
        raise Exception("Only .tb TigerByte files are supported")
    if not os.path.exists(filepath):
        raise Exception(f"File not found: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        source = f.read()
    lexer = Lexer(source)
    parser = Parser(lexer)
    stmts = parser.parse()
    interp = Interpreter()
    for s in stmts:
        interp.visit(s)

def main():
    parser = argparse.ArgumentParser(description="🐯 TigerByte Interpreter")
    
    # 1. ADD THE NEW BANNER ARGUMENT
    parser.add_argument(
        '--banner', 
        type=str, 
        nargs='?', 
        const='random', 
        default='random', 
        help="Specify a banner name (e.g., 'banner1.txt') or 'none' to hide it. Default is 'random'."
    )
    
    # 2. KEEP THE ORIGINAL FILE ARGUMENT
    parser.add_argument("file", help="path to .tb file")

    # 3. USE parse_known_args() TO ALLOW OTHER ARGS
    args, _ = parser.parse_known_args()

    # 4. ADD THE BANNER DISPLAY LOGIC
    if args.banner != 'none':
        if args.banner == 'random':
            display_random_banner()
        else:
            display_banner_by_name(args.banner)
            
    # 5. KEEP THE ORIGINAL CALL TO RUN THE FILE
    run_tigerbyte_file(args.file)

if __name__ == "__main__":
    main()