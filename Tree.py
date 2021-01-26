from Node import Node

class Tree:
    def __init__(self, root:Node=None):
        self.root = root
        self.nodes = []

    def parse(self):
        self.root.parse()
    
    def insert(self):
        self.root.insert()