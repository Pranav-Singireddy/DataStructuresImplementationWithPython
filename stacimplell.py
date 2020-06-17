class node():
    def __init__(self,value):
        self.node={'value':value,'next':None}
    def __str__(self):
        return(str(self.node))
class stack():
    def __init__(self):
        self.top=None
        self.bottom=None
        self.length=0
    def __str__(self):
        return(str(self.__dict__))
    def push(self,value):
        newnode={'value':value,'next':None}
        if(self.length==0):
            self.top=newnode
            self.bottom=newnode
            self.length+=1
        else:
          k=self.top
          self.top=newnode
          self.top['next']=k
          self.length+=1
        return(self)
    def peek(self):
        print(self.top['value'])
    def pop(self):
        p=self.top
        self.top=p['next']
        del p
        self.length-=1
        return(self)
k=stack()
k.push(0)
k.push(1)
k.push(2)
k.peek()
print(k)
k.pop()
print(k)
        
        
