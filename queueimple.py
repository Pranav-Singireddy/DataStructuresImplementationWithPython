class queue():
    def __init__(self):
        self.top=None
        self.bottom=None
        #self.new={}
        self.length=0
    def __str__(self):
        return(str(self.__dict__))
    def enqueue(self,value):
        self.new={'value':value,'next':None}
        if(self.length==0):
            self.top=self.new
            self.bottom=self.new
            self.length+=1
        else:
         self.top['next']=self.new
         self.top=self.new
         self.length+=1
        return(self)
    def peek(self):
        print(self.top)
    def dequeue(self):
        k=self.bottom
        self.bottom=k['next']
        del k
        self.length-=1
        return(self)
q=queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)  #in stack newnode next is changed but in queue top next is changed
q.enqueue(4)  #stack-4,3,2,1 queue-1,2,3,4 in both top n bottom are same but 
q.peek()      #the order of arrangement is different
print(q)
q.dequeue()
print(q)

         
        
        
