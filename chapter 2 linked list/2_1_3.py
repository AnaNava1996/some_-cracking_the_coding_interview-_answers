#the same but with actually a simple linked list
#deleting the element without extra space but more time consuming

class Node:
    def __init__(self,value):
        self.next=None
        self.value=value
 

class Stack:
    def __init__(self):
        self.head=None
        self.top=None

    def add_value(self,value):#constant complexity
        newNode=Node(value)
        if(self.head is None):
            self.head=newNode
            self.top=self.head
        else:
            self.top.next=newNode
            self.top=self.top.next
            
    def print_stack(self):#lineal complexity
        aux=self.head
        print("")
        while(aux!=None):
            print(aux.value,end="   ")
            aux=aux.next
        print("")

    def print_top(self):#constant
        if(self.top==None):
            print("Error")
        else:
            print(self.top.value)

    def pop(self):#lineal
        if(self.head==self.top):
            self.head=None
        else:
            aux=self.head
            while(aux.next!=self.top):
                aux=aux.next
            aux.next=None
            self.top=aux
            
    def delete_repetitions(self):   #0(n²)    :(
        if(self.head==self.top):
            print("no repetitions")
        else:
            a=self.head
            while(a!=self.top and a!=None):
                b=a
                while(b.next!=None):
                    if(a.value == b.next.value):
                        if(b.next==self.top):
                            b.next=b.next.next
                            self.top=b
                        else:
                            b.next=b.next.next
                    else:
                        b=b.next
                a=a.next
                              


stackie=Stack()

stackie.add_value(5)
stackie.add_value(5)
stackie.add_value(5)
#stackie.add_value(10)
#stackie.add_value(2)
#stackie.add_value(3)
#stackie.add_value(5)
#stackie.add_value(4)



stackie.print_stack()
stackie.print_top()
'''
stackie.pop()
stackie.print_stack()
stackie.print_top()

stackie.pop()
stackie.print_stack()
stackie.print_top()

stackie.pop()
stackie.print_stack()
stackie.print_top()
'''

stackie.delete_repetitions()
stackie.print_stack()

#functions of a stack
#add_node    
#pop
#push
#top
#is_empty
#read_stack







