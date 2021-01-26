import sys
import re

token_expressions=[(r'.+;',"COMMAND")
,(r'[ \n\t]+',None)
,(r'#[^\n]*',None)
,(r'IF',"IF")
,(r'THEN',"THEN")s
,(r'ELSE',"ELSE")
,(r'END',"END")
,(r"\w+(==|>|<|<=|>=)\w+","COND")
]

src = """
a=2;
b=3;
c=4;
IF a>b THEN
        total := total + price * quantity;
        tax := price * 0.05;
        ELSE IF a<b THEN
            total = total - price;
            tax--;
        ELSE
            a++;
        END
    END
b=12;
"""

class Token:
    def __init__(self,text, tag):
        self.text = text
        self.tag = tag
    def __repr__(self):
        return str((self.text , self.tag))

def lex(characters, token_exprs):
    pos = 0
    tokens = []
    while pos < len(characters):
        match = None
        for token_expr in token_exprs:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = Token(text, tag)
                    tokens.append(token)
                break
        if not match:
            sys.stderr.write('Illegal character: %s\\n' % characters[pos])
            sys.exit(1)
        else:
            pos = match.end(0)
    return tokens
