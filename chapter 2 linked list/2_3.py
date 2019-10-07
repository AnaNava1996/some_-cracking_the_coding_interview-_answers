class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    

class Single_linked_list:
    def __init__(self):
        self.head=None
        self.top=None
    
    def add_data(self,data):
        newNode=Node(data)
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
            print(aux.data,end="   ")
            aux=aux.next
        print("")

    def delete_node(self,node):#time complexity = O(1)
        if(node==self.head or node==self.top):
            print("cannot delete that")
        else:
            node.data=node.next.data
            node.next=node.next.next

        
la_lista=Single_linked_list()
la_lista.add_data(1)
la_lista.add_data(2)
la_lista.add_data(3)
la_lista.add_data(4)
la_lista.add_data(5)
la_lista.print_list()


la_lista.delete_node(la_lista.head.next.next.next.next)
la_lista.print_list()

la_lista.delete_node(la_lista.head.next.next.next)
la_lista.print_list()











