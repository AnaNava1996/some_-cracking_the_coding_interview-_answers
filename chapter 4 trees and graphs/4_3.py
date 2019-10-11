#4.3   List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
#at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
#############################################################################################################


#an empty list... of nodes
alist=list()

class Tree_Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class List_Node:
    def __init__(self,node):
        self.node=node
        self.next=None
class Linked_list:
    def __init__(self):
        self.head=None
        self.top=None
    def insert_node(self,node):
        newNode=List_Node(node)
        if(self.head==None):
            self.head=newNode
            self.top=self.head
        else:
            self.top.next=newNode
            self.top=self.top.next
    def print_list(self):
        aux=self.head
        print("")
        while(aux!=None):
            print(aux.node.data,end="  ")
            aux=aux.next
        print("")

def the_function(node,index):
    if(len(alist)<index+1):
        newList=Linked_list()
        newList.insert_node(node)
        alist.append(newList)
    else:
        alist[index].insert_node(node)
    if(node.left!=None):
        the_function(node.left,index+1)
    if(node.right!=None):
        the_function(node.right,index+1)

node1=Tree_Node(5)
node2=Tree_Node(3)   
node3=Tree_Node(8)   
node4=Tree_Node(2)   
node5=Tree_Node(4)   
node6=Tree_Node(7)   
node7=Tree_Node(9)   
node8=Tree_Node(1)   
node9=Tree_Node(6)   

node1.left=node2
node1.right=node3
node2.left=node4
node2.right=node5
node4.left=node8
node3.left=node6
node3.right=node7
node6.left=node9


the_function(node1,0)

for i in alist:
    i.print_list()

'''
def preorder(node):#root, left,right
    print(node.data,end="  ")
    if(node.left!=None):
        preorder(node.left)
    if(node.right!=None):
        preorder(node.right)

def postorder(node):#left,right,root
    if(node.left!=None):
        postorder(node.left)
    if(node.right!=None):
        postorder(node.right)
    print(node.data,end="  ")

def inorder(node):#left,root,right
    if(node.left!=None):
        inorder(node.left)
    print(node.data,end="  ")
    if(node.right!=None):
        inorder(node.right)

preorder(node1)
print("")
postorder(node1)
print("")
inorder(node1)


'''



  
