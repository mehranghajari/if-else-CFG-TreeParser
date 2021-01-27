from lexer import lex, token_expressions,src
from Node import Tag, Node
from Tree import Tree
from graphviz import Digraph,Graph

if __name__ == "__main__":
    tokens = lex(src,token_expressions)
    root = Node(tokens, Tag.STATEMENT)
    tree  = Tree(root)
    tree.parse()
    # print("pre:")
    # tree.root.pre_order()
    # print("post:")
    # tree.root.post_order()
    # dot = Digraph('G',format='png')

    dot = Digraph('G',format='png')
    tree.root.add_node(dot,1)
    dot.render()
    print("NT: ")
    tree.root.print_non_terminals()
    print("Terminal")
    tree.root.print_terminals()