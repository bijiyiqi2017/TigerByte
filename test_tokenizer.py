import unittest
from tokenizer import Tokenizer, Token, TOKEN_TYPES

class TestTokenizer(unittest.TestCase):

    def test_single_keyword_and_number(self):
        """Tests the basic 'print 42' functionality."""
        code = "print 42"
        tokenizer = Tokenizer(code)
        tokens = tokenizer.tokenize()
        
        expected = [
            Token(TOKEN_TYPES['KEYWORD'], 'print'),
            Token(TOKEN_TYPES['NUMBER'], 42),
            Token(TOKEN_TYPES['EOF'], None)
        ]
        self.assertEqual(tokens, expected)

    def test_arithmetic_expression(self):
        """Tests handling of numbers and operators."""
        code = "10 + 5 * (7 - 2)"
        tokenizer = Tokenizer(code)
        tokens = tokenizer.tokenize()
        
        expected = [
            Token(TOKEN_TYPES['NUMBER'], 10),
            Token(TOKEN_TYPES['OPERATOR'], '+'),
            Token(TOKEN_TYPES['NUMBER'], 5),
            Token(TOKEN_TYPES['OPERATOR'], '*'),
            Token(TOKEN_TYPES['OPERATOR'], '('),
            Token(TOKEN_TYPES['NUMBER'], 7),
            Token(TOKEN_TYPES['OPERATOR'], '-'),
            Token(TOKEN_TYPES['NUMBER'], 2),
            Token(TOKEN_TYPES['OPERATOR'], ')'),
            Token(TOKEN_TYPES['EOF'], None)
        ]
        self.assertEqual(tokens, expected)

    def test_identifier_and_assignment_and_keyword(self):
        """Tests identifiers and a mix of types."""
        code = "result = print value"
        tokenizer = Tokenizer(code)
        tokens = tokenizer.tokenize()
        
        expected = [
            Token(TOKEN_TYPES['IDENTIFIER'], 'result'),
            Token(TOKEN_TYPES['OPERATOR'], '='),
            Token(TOKEN_TYPES['KEYWORD'], 'print'),
            Token(TOKEN_TYPES['IDENTIFIER'], 'value'),
            Token(TOKEN_TYPES['EOF'], None)
        ]
        self.assertEqual(tokens, expected)

    def test_unknown_symbols(self):
        """Tests handling of characters not defined as part of the language."""
        code = "! # $"
        tokenizer = Tokenizer(code)
        tokens = tokenizer.tokenize()

        expected = [
            Token(TOKEN_TYPES['UNKNOWN'], '!'),
            Token(TOKEN_TYPES['UNKNOWN'], '#'),
            Token(TOKEN_TYPES['UNKNOWN'], '$'),
            Token(TOKEN_TYPES['EOF'], None)
        ]
        self.assertEqual(tokens, expected)

if __name__ == '__main__':
    unittest.main()