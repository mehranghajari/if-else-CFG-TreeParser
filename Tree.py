from Node import Node

class Tree:
    def __init__(self, root:Node=None):
        self.root = root
        
    def parse(self):
        self.root.parse()
    
    # def insert(self):
    #     self.root.insert()

    def print(self):
        self.root.print()

    def add_graph(self,graph,i):
        self.root.add_graph(graph,i)