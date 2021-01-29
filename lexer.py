import sys
import re

token_expressions=[(r'.+;',"COMMAND")
,(r'[ \n\t]+',None)
,(r'#[^\n]*',None)
,(r'IF',"IF")
,(r'THEN',"THEN")
,(r'ELSE',"ELSE")
,(r'END',"END")
,(r"\w+ *(==|>|<|<=|>=) *\w+","COND")
]

src = """
a=2;
b=3;
c=4;
IF a>1 THEN
    IF a>2 THEN
        IF a>3 THEN
            salsabil+sagsibil;
            IF a>4 THEN
                a--;
                b--;
                    IF a>5 THEN
                    a-5;
                    a-5;
                    ELSE
                    a+5;
                    a+5;
                    END
                a-4;
                a-4;
                    ELSE IF space == bishuuuur THEN
                    a+4;
                    a+4;
                    END
                ablabloo;
            END
            a-3;
            a+3;
            ELSE
            a-3;
            a+3;

        a-2;
        b-2;
        ELSE IF s==52 THEN
        a+2;
        END
    END
    a-1;
    ELSE
    a+1;
END
a;
IF baaabuuuuu>5 THEN
KHAAAAAAAAAAK;
END
"""

# src = """
# SHORUU;
# IF a>b THEN
# bozorgtar;
# IF a>=b THEN
# bozorgtarmosavi;
# END
# ccc;
# END
# IF b>a THEN
# kooochiktar;
# END
# PAAYAAN;
# IF c>cc THEN
# cccc;
# END
# """


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
