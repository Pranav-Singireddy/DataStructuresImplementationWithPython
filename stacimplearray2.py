class stack():
    def __init__(self):
        self.arr=[]
    def __str__(self):
        return(str(self.arr))
    def push(self,value):
        self.arr.append(value)
        return(self)
    def peek(self):
        print(self.arr[len(self.arr)-1])
    def pop(self):
        self.arr.pop()
        return(self)
d=stack()
d.push(1)
d.push(2)
d.push(3)
d.push(4)
d.peek()
print(d)
d.pop()
print(d)
