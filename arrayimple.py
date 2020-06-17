class myarray():
    def __init__(self):
        self.arr={}
        self.length=0
    def __str__(k):
        return str(k.__dict__)
    def push(self,value):
        index=self.length
        self.arr[index]=value
        self.length+=1
        #print(index,self.length)
    def print(self):
        sel=1
        print(self.arr)
    def pop(self):
        last=self.arr[self.length-1]
        del self.arr[self.length-1]
        self.length-=1
        print(last)
    def delete(self,index):
        deli=self.arr[index]
        for i in range(index,self.length-1):
            self.arr[i]=self.arr[i+1]
        del self.arr[self.length-1]
        self.length-=1
        print(deli)
    def lookup(self,index):
        print(self.arr[index])
fg=myarray()
fg.push('hi')
fg.push(2)
fg.push('this')
fg.push(3)
fg.pop()
fg.push(3)
fg.delete(1)
fg.lookup(1)
print(fg)


