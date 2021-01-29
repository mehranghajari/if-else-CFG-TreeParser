from lexer import lex, token_expressions
from Node import Tag, Node
from Tree import Tree

if __name__ == "__main__":
    with open('input.txt','r') as src:
        src_string = src.read()
        tokens = lex(src_string,token_expressions)
        root = Node(tokens, Tag.STATEMENT)
        tree  = Tree(root)
        tree.parse()
        tree.print()
    # to enable graphics uncomment these:
    # you must have graphviz and the graphviz python package installed 
        # from graphviz import Digraph,Graph
        # dot = Digraph('AST-ish',format='png')
        # tree.root.add_node(dot)
        # dot.render()
