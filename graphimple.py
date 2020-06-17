class graph():
    def __init__(self):
        self.node={}
        self.numnodes=0
    def __str__(self):
        return(str(self.__dict__))
    def addvertex(self,value):
        self.node[value]=[]
        self.numnodes+=1
        return(self)
    def addedge(self,node1,node2):
        self.node[node1].append(node2)
        self.node[node2].append(node1)
        return(self)
    def showconnection(self):
     for x in self.node.keys():
      print(x , end = '-->')
      for i in self.node[x]:
        print(i , end = ' ') 
      print()
g=graph()
g.addvertex('0')
g.addvertex('1')
g.addvertex('2')
g.addvertex('3')
g.addvertex('4')
g.addvertex('5')
g.addvertex('6')
g.addedge('3','1')
g.addedge('0','1')
g.addedge('3','2')
g.addedge('4','5')
g.addedge('6','5')
g.addedge('3','6')
g.addedge('4','2')
g.showconnection()
#print(g)
