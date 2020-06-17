import json
class node():
    def __init__(self,value):
        self.left=None
        self.right=None
        self.value=value
class binaryst():
    def __init__(self):
        self.root=None
    def __str__(self):
        return("x:% s" % (self.root))
    def insert(self,value):
        new=node(value)
        if(self.root==None):
          self.root=new
          return
        else:
            cur=self.root
            while(True):
                if(value<cur.value):
                    if(cur.left==None):
                        cur.left=new
                        return(self)
                    cur=cur.left
                elif(value>cur.value):
                    if(cur.right==None):
                        cur.right=new
                        return(self)
                    cur=cur.right
        return(self)
    def lookup(self,value):
        cur=self.root
        
        while(True):
            if(cur ==None):
             return(False)
            
            if(value<cur.value):
                cur=cur.left
            elif(value>cur.value):
                cur=cur.right
            elif(value==cur.value):
                return(True)
    def print_tree(self):
     if self.root != None:
      self.printt(self.root)
#Inorder Traversal (We get sorted order of elements in tree)

    def printt(self,curr_node):
     if curr_node != None:
      self.printt(curr_node.left)
      print(str(curr_node.value))
      self.printt(curr_node.right)
                
b=binaryst()
b.insert(20)
b.insert(30)
b.insert(12)
y=b.lookup(20)
print(y)
z=b.lookup(211)
print(z)
b.print_tree()
