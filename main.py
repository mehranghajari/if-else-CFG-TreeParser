from lexer import lex, token_expressions,src
from Node import Tag, Node
from Tree import Tree

if __name__ == "__main__":
    tokens = lex(src,token_expressions)
    root = Node(tokens, Tag.STATEMENT)
    tree  = Tree(root)
    tree.parse()

    