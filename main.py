from lexer import lex, token_expressions,src
from Node import Tag, Node
from Tree import Tree
from graphviz import Digraph

if __name__ == "__main__":
    tokens = lex(src,token_expressions)
    root = Node(tokens, Tag.STATEMENT)
    tree  = Tree(root)
    tree.parse()
    # print("pre:")
    # tree.root.pre_order()
    # print("post:")
    # tree.root.post_order()
    
    