#Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.



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
    
    #time cplexity O(n)
    #1- iterate thru the elements to count the elements
    #2- iterate another time to the (numer_of_elements - k) position
    def the_trivial_one(self,k):
        cont=0
        aux=self.head
        while(aux!=None):
            cont = cont+1
            aux=aux.next
        if(cont < k):
            print("cannot do that")
            return
        else:
            aux2=self.head
            cont=cont-k
            while(cont!=0):
                cont-=1
                aux2=aux2.next
            return aux2.data
            


tha_list=Single_linked_list()

tha_list.add_value(5)
tha_list.add_value(2)
tha_list.add_value(4)
tha_list.add_value(1)
tha_list.add_value(9)
tha_list.add_value(0)
tha_list.add_value(7)
tha_list.add_value(4)
tha_list.add_value(3)
tha_list.add_value(2)


tha_list.print_list()
print(tha_list.the_trivial_one(4))

