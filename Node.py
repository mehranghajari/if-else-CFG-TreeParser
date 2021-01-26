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
                    if_stmt.insert(0,("IF","IF"))
                    child = Node(body = (if_stmt),tag = Tag.IF_STATEMENT)
                    self.children.append(child)
                    i=j
                    child.parse()
                    print("IF_STMT")
                elif token.tag == 'COMMAND':
                    print(token.text)
                    self.children.append(Node(body=[token.text],tag=Tag.TERMINAL))
                i+=1
        elif(self.tag == Tag.IF_STATEMENT):
            #print(self.body)

            i=0
            while i < len(self.body):
            #     token = self.body[i]
            #     if i < 3:
            #         child  = Node(body=token., tag = tag.TERMINAL)
            #         self.children.append(child)
            #     else:
            #         token = self.body[i:]
            #i+=1
            #print(self.children[0].body)
            # A -> sbfH
            # IF_STMT -> if (condition) then STMT ELSE STMT
    # if tag is statement
        #parse body of node [If Cond Else .....]
        # read elements
            # if element if 
                # insert a node of IF Type 
            # Cond
                # ...... Cond Type
            # Every statements ---> 
        
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
        return self.body[j:i+1], i
    

