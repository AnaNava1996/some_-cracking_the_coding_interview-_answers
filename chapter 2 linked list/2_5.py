class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Single_linked_list:
    def __init__(self):
        self.head=None
        self.top=None

    def add_value(self,data):#constant complexity
        newNode=Node(data)
        if(self.head is None):
            self.head=newNode
            self.top=self.head
        else:
            self.top.next=newNode
            self.top=self.top.next
            
    def print_list(self):#lineal complexity
        aux=self.head
        print("")
        while(aux!=None):
            print(aux.data,end="   ")
            aux=aux.next
        print("")
 
def the_sum(list1, list2):
    list3=Single_linked_list()
    node1=list1.head
    node2=list2.head
    list3.add_value(0)
    node3=list3.head
    while(node1!=None or node2!=None):
        if(node1==None):
            new_value=node3.data + node2.data
            node3.data = newValue%10
            list3.add_value(new_value//10)
            node3=node3.next
            node2=node2.next
        elif(node2==None):
            new_value=node3.data + node1.data
            node3.data = new_value%10
            list3.add_value(new_value//10)
            node3=node3.next
            node1=node1.next
        else:
            new_value=node3.data + node1.data + node2.data
            print(new_value)
            node3.data=new_value%10
            list3.add_value(new_value//10)
            node3=node3.next
            node1=node1.next
            node2=node2.next
    list3.print_list()
    return list3


 
list1=Single_linked_list()
list1.add_value(7)
list1.add_value(1)
list1.add_value(6)
list2=Single_linked_list()
list2.add_value(5)
list2.add_value(9)
list2.add_value(2) 


listica=the_sum(list1,list2)









