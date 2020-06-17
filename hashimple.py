import random 
class myhash():
    def __init__(self):
        self.size=int(input())
        self.data=['' for i in range(self.size)]
        self.addrl=[]
    def __str__(self):
        return( str(self.data))
    def _hashfunc(self,key):
         q=0
         for i in range(0,len(key)):
          q=(q+ord(key[i])*i)%(self.size)
         #if q not in self.addrl:
            #self.addrl.append(q)
         return(q)
    def seth(self,key,value):
        addr=self._hashfunc(key)
        print(addr)
        self.data[addr]=[key,value]
        self.addrl.append(addr)
        #print(self.data)
    def geth(self,key):
        addr1=self._hashfunc(key)
        print(addr1)
        if(self.data[addr1][0]==key):
                print(self.data[addr1][1])
                
   # def keysh(self):
       # l=[]
        #for i in self.addrl:
           # l.append(self.data[i][0])
        #print(l)
    
        
k=myhash()
k.seth('grapes',1000)
k.seth('grapes',1001)
k.seth('apples',1200)
k.seth('asses',1400)
k.geth('grapes')
#k.keysh()
print(k)

    
