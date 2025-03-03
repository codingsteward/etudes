from typing import Any
from tokentype import TokenType
class Token:

    def __init__(self, token_t: TokenType, lexeme: str, literal: Any, line: int):
        self.token_t = token_t
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

token = Token(TokenType.LEFT_PAREN, "(", None, 1)
print(token)
