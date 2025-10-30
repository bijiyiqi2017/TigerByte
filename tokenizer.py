from typing import List, NamedTuple, Dict, Any

# 1. Define the Token Structure
# A NamedTuple provides a simple, structured object for tokens.
class Token(NamedTuple):
    """Represents a single lexical unit in the TigerByte language."""
    type: str
    value: Any
    # Optional: line: int # Can be added later for advanced error reporting

# 2. Define Token Types and Reserved Keywords
# Note: Token types are often uppercase strings.
TOKEN_TYPES: Dict[str, str] = {
    'KEYWORD': 'KEYWORD',
    'IDENTIFIER': 'IDENTIFIER',
    'NUMBER': 'NUMBER',
    'OPERATOR': 'OPERATOR',
    'WHITESPACE': 'WHITESPACE', # We will usually ignore this
    'EOL': 'EOL', # End of line/statement delimiter
    'EOF': 'EOF', # End of file/input
    'UNKNOWN': 'UNKNOWN'
}

# Supported Keywords (Required for 'print' command)
RESERVED_KEYWORDS: Dict[str, str] = {
    'print': TOKEN_TYPES['KEYWORD'],
    # 'if': TOKEN_TYPES['KEYWORD'], # Stretch goals can be added later
}

# 3. The Tokenizer Class
class Tokenizer:
    def __init__(self, source_code: str):
        self.source_code = source_code
        self.position = 0
        self.tokens: List[Token] = []

    def _get_current_char(self) -> str | None:
        """Returns the character at the current position, or None if EOF."""
        if self.position < len(self.source_code):
            return self.source_code[self.position]
        return None

    def _advance(self) -> None:
        """Moves the tokenizer's position to the next character."""
        self.position += 1

    def _skip_whitespace(self) -> None:
        """Skips over consecutive whitespace characters."""
        while self._get_current_char() is not None and self._get_current_char().isspace():
            self._advance()

    def _tokenize_word_or_keyword(self) -> Token:
        """Tokenizes an identifier or a reserved keyword (like 'print')."""
        start_pos = self.position
        
        # Read all consecutive alphanumeric characters
        while self._get_current_char() is not None and self._get_current_char().isalnum():
            self._advance()
        
        # Extract the word
        value = self.source_code[start_pos:self.position]
        
        # Check if the word is a reserved keyword
        token_type = RESERVED_KEYWORDS.get(value, TOKEN_TYPES['IDENTIFIER'])
        
        return Token(token_type, value)

    def _tokenize_number(self) -> Token:
        """Tokenizes a number (integer only for simplicity)."""
        start_pos = self.position
        
        # Read all consecutive digits
        while self._get_current_char() is not None and self._get_current_char().isdigit():
            self._advance()
        
        value = self.source_code[start_pos:self.position]
        
        # Convert value to integer (or float, if required later)
        return Token(TOKEN_TYPES['NUMBER'], int(value))

    def _tokenize_operator(self) -> Token:
        """Tokenizes a single-character operator."""
        char = self._get_current_char()
        self._advance()
        
        # For simplicity, we only handle single-character operators now
        # Multi-character operators (==, >=) can be added here later.
        return Token(TOKEN_TYPES['OPERATOR'], char)

    def tokenize(self) -> List[Token]:
        """Main method to break the entire source code into tokens."""
        operators = ['+', '-', '*', '/', '=', '(', ')', '<', '>']
        
        while self.position < len(self.source_code):
            char = self._get_current_char()
            
            if char is None:
                break
            
            if char.isspace():
                self._skip_whitespace()
                continue # Do not create a token for whitespace
            
            if char.isalpha():
                token = self._tokenize_word_or_keyword()
                self.tokens.append(token)
                continue
            
            if char.isdigit():
                token = self._tokenize_number()
                self.tokens.append(token)
                continue
                
            if char in operators:
                token = self._tokenize_operator()
                self.tokens.append(token)
                continue
                
            # If the character is none of the above, it's an unknown symbol
            self.tokens.append(Token(TOKEN_TYPES['UNKNOWN'], char))
            self._advance()

        # Add End of File token at the end
        self.tokens.append(Token(TOKEN_TYPES['EOF'], None))
        
        return self.tokens

if __name__ == '__main__':
    # Example usage and proof (Optional Documentation / Proof)
    sample_code = "print 42 + result"
    tokenizer = Tokenizer(sample_code)
    tokens = tokenizer.tokenize()
    
    print(f"--- Sample Input: '{sample_code}' ---")
    for token in tokens:
        print(f"Type: {token.type:<12} Value: {token.value}")

    # Expected Output:
    # Type: KEYWORD      Value: print
    # Type: NUMBER       Value: 42
    # Type: OPERATOR     Value: +
    # Type: IDENTIFIER   Value: result
    # Type: EOF          Value: None