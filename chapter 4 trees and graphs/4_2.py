class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.root=None

def print_preorder(node):
    print(node.data)
    if(node.left!=None):
        print_preorder(node.left)
    if(node.right!=None):
        print_preorder(node.right)


def conecting_nodes(a_list,flag,tree):
    if(len(a_list)==0):
        print("empty tree")
    else:
        index = len(a_list)//2
        new_node=Node(a_list[index])
        if(flag==1):
            flag=0
            tree.root=new_node
        if(len(a_list)>=3):
            new_node.left=conecting_nodes(a_list[0:index],flag,tree)
            new_node.right=conecting_nodes(a_list[index+1:],flag,tree)
        elif(len(a_list)==2):
            new_node.left=conecting_nodes(a_list[0:index],flag,tree)
        return new_node

tree_1= Tree()
a_list=[1,2,3,4,5,6,7,8,9]
tree_1.root=conecting_nodes(a_list,1,tree_1)
print(tree_1.root.data)

print_preorder(tree_1.root)#5,3,2,1,4,8,7,6,9



