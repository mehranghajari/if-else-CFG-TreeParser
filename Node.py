from enum import Enum
from collections import deque as queue
class Tag(Enum):
    STATEMENT = 1
    TERMINAL  = 2
    IF_STATEMENT = 3 

class Node:
    index = 0
    def __init__(self,body=[], tag=None):
        self.body = body
        self.tag = tag
        self.i = 0
        self.children = []

    def is_leaf(self):
        return self.children is [] 

    def parse(self):
        if(self.tag == Tag.STATEMENT):
            if not self.body :
                return    
            token = self.body[0]
            if token.tag == 'IF'  :
                if_stmt , j = self.create_if_statement_body(1)
                self.add_child(if_stmt,Tag.IF_STATEMENT,True)
                if not self.body[j:]:
                    return
                self.add_child(self.body[j:],Tag.STATEMENT,True)

            elif token.tag == 'COMMAND':
                self.add_child([token.text],Tag.TERMINAL,False)
                if not self.body[1:]:
                    return
                self.add_child(self.body[1:],Tag.STATEMENT,True)
            
            else:
                next_stmt = self.body[1:]
                if not next_stmt:
                    self.add_child(['ε'],Tag.TERMINAL,False)
                else:
                    self.add_child(self.body[1:],Tag.STATEMENT,True)

        elif(self.tag == Tag.IF_STATEMENT):
            i=0
            while i < len(self.body):
                token = self.body[i]
                if i < 3:
                    self.add_child([token.text],Tag.TERMINAL,False)
                else:
                    stmt, i = self.endOfStatement(i)
                    self.add_child(stmt,Tag.STATEMENT,True)
                    if i < len(self.body):
                        token = self.body[i]
                        self.add_child([token.text],Tag.TERMINAL)
                        i+=1
                        stmt, i = self.endOfStatement(i)
                        self.add_child(stmt,Tag.STATEMENT,True)
                        
                i+=1
    
    def create_if_statement_body(self, i):
        c = 0
        j = i
        while i < self.body.__len__() :
            if self.body[i].tag == "IF":
                c+=1
            if self.body[i].tag == "END":
                if c > 0:
                    c-=1
                else:
                    break
            i+=1
        return self.body[j-1:i+1], i+1
    
    def endOfStatement(self, i):
        c = 0
        j = i
        while i < self.body.__len__() :
            if self.body[i].tag == "IF":
                c+=1
            if self.body[i].tag == "END":
                if c > 0:
                    c-=1
                else:
                    break
            if self.body[i].tag =="ELSE" and c==0:
                break    
            i+=1
        return self.body[j:i],i



    def add_edge(self, graph,index,child_index):
        graph.edge(str(index),str(child_index))

    def add_child(self, body, tag, parse:bool = False):
        child = Node(body,tag)
        Node.index+=1
        child.i = Node.index
        self.children.append(child)
        child.parse()

    def add_node(self,graph):
        if self.tag == Tag.TERMINAL:
            graph.node(str(self.i),str(self.body[0]))
        else:
            graph.node(str(self.i),str(self.tag.name))
        for child in self.children:
            child.add_node(graph)
            self.add_edge(graph,self.i,child.i)
        
