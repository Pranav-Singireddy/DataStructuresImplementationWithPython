#class node():
    #def __init__(self,value):
      #  self.value=value
        #self.next=None
class linkedlist():
    def __init__(self,value1):
        self.head={'value': value1,'next':None}
        self.tail=self.head
        self.length=1
    def __str__(self):
        return(str(self.__dict__))
    def append(self,value):
        self.newnode={'value':value,'next':None}#for all new nodes we can also utilize the above node class
        self.tail['next']=self.newnode#first tail value will be updated ..since it is pointing to same pointer as head ..head value will also be altered.
        self.tail=self.newnode#now tail value is updated.
        self.length+=1
        return(self)
    def prepend(self,value):
        self.newnode1={'value':value,'next':None}#next:self.head can also be used.
        self.newnode1['next']=self.head#first newnode pointer is updated with head
        self.head=self.newnode1#now new head is newnode
        self.length+=1
        return(self)
    def display(self):
        self.k=[]
        self.cur=self.head
        while(self.cur != None):
            self.k.append(self.cur['value'])
            self.cur=self.cur['next']
        print(self.k)
    def insert(self,index,value):
        self.newnode2={'value':value,'next':None}
        if(index>=self.length):
            self.append(value)
        elif(index==0):
            self.prepend(value)
        else:
         self.leader=self.traversetoindex(index-1)
         self.holder=self.leader['next']
         self.leader['next']=self.newnode2
         self.newnode2['next']=self.holder
         self.length+=1
        return(self)
    def traversetoindex(self,index):
        total=0
        self.cur=self.head
        while(total != index):
            self.cur=self.cur['next']
            total+=1
        return(self.cur)
    def remove(self,index):
        self.point=self.traversetoindex(index)
        if(index==0):
            del self.point
            self.head=self.traversetoindex(index+1)
            self.length-=1
        elif(index==self.length):
            del self.point
            self.tail=self.traversetoindex(index-1)
            self.length-=1
        else:
         self.leader1=self.traversetoindex(index-1)
         self.holder1=self.point['next']
         del self.point
         self.leader1['next']=self.holder1
         self.length-=1
        return(self)
lk=linkedlist(2)
lk.append(6)
lk.prepend(3)
lk.display()
lk.insert(20,10)
lk.display()
lk.remove(3)
lk.display()
print(lk)
