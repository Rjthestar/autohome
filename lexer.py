import re
from dataclasses import dataclass
from typing import List, Optional


class TokenType:
    KEYWORD = "KEYWORD"
    IDENTIFIER = "IDENTIFIER"
    NUMBER = "NUMBER"
    STRING = "STRING"
    OPERATOR = "OPERATOR"
    UNKNOWN = "UNKNOWN"


@dataclass
class Token:
    type: str
    value: str


RULES = [
    {"regex": r"\s+", "type": None},  
    {"regex": r"//.*", "type": None},  
    
    {"regex": r"\b(TURN|LIGHTS|ON|OFF|SET)\b", "type": TokenType.KEYWORD},
    {"regex": r"[a-zA-Z_]\w*", "type": TokenType.IDENTIFIER},
    {"regex": r"\d+(\.\d+)?", "type": TokenType.NUMBER},
    {"regex": r"\".*?\"", "type": TokenType.STRING},
    {"regex": r"[+\-*/=]", "type": TokenType.OPERATOR},
]



def tokenize(code: str) -> List[Token]:
    tokens = []
    i = 0

    while i < len(code):
        match_found = False

        for rule in RULES:
            pattern = re.compile(rule["regex"])
            match = pattern.match(code, i)

            if match:
                text = match.group(0)

                if rule["type"]:  # ignore None types
                    tokens.append(Token(rule["type"], text))

                i += len(text)
                match_found = True
                break

        if not match_found:
            tokens.append(Token(TokenType.UNKNOWN, code[i]))
            i += 1

    return tokens