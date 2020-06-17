class stack():
    def __init__(self):
        self.top=None
        self.bottom=None
        self.newele={}
        self.length=0
    def __str__(self):
        return(str(self.__dict__))
    def push(self,value):
        index=self.length
        self.newele[index]=value
        if(index==0):
            self.top=self.newele[index]
            self.bottom=self.newele[index]
            self.length+=1
        else:
          self.top=self.newele[index]
          self.length+=1
        return(self)
    def peek(self):
        print(self.newele[self.length-1])
    def pop(self):
        del self.newele[self.length-1]
        self.length-=1
        self.top=self.newele[self.length-1]
        return(self)
o=stack()
o.push(10)
o.push(11)
o.push(12)
o.peek()
print(o)
o.pop()
print(o)
          
        
