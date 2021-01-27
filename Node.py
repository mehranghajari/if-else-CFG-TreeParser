from enum import Enum
class Tag(Enum):
    STATEMENT = 1
    TERMINAL  = 2
    IF_STATEMENT = 3 

class Node:
    def __init__(self,body=[], tag=None):
        self.body = body
        self.tag = tag
        self.children = []

    def is_leaf(self):
        return self.children is [] 

    def parse(self):
        if(self.tag == Tag.STATEMENT):
            i=0
            while  i < len(self.body):
                token = self.body[i]
                if token.tag == 'IF'  :
                    if_stmt , j = self.create_if_statement_body(i+1)
                    child = Node(body = (if_stmt),tag = Tag.IF_STATEMENT)
                    self.children.append(child)
                    i=j
                    child.parse()
                elif token.tag == 'COMMAND':
                    self.children.append(Node(body=[token.text],tag=Tag.TERMINAL))
                i+=1
        elif(self.tag == Tag.IF_STATEMENT):
            i=0
            while i < len(self.body):
                token = self.body[i]
                if i < 3:
                    child  = Node(body=[token.text], tag = Tag.TERMINAL)
                    self.children.append(child)
                else:
                    stmt, i= self.endOfStatement(i)
                    child = Node(body=stmt, tag=Tag.STATEMENT)
                    self.children.append(child)
                    child.parse()
                    if i != len(self.body)-1:
                        token=self.body[i]
                        child = Node(body=[token.text],tag =Tag.TERMINAL)
                        i+=1
                        stmt, i= self.endOfStatement(i)
                        child = Node(body=stmt, tag=Tag.STATEMENT)
                        self.children.append(child)
                        child.parse()
                i+=1

    
    def create_if_statement_body(self, i):
        c = 0
        j = i
        counter=0
        while i < self.body.__len__() :
            if self.body[i].tag == "IF":
                c+=1
            if self.body[i].tag == "END":
                if c > 0:
                    c-=1
                else:
                    break
            i+=1
        return self.body[j-1:i+1], i
    
    def endOfStatement(self, i):
        c = 0
        j = i
        counter=0
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

    def add_node(self, graph,i):
        graph.node(str(i),'yoyo')
        for child in self.children:
            child.add_node(graph,i+1)