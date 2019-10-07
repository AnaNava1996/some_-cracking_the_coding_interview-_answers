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
    
    
    #while i haven't reached the Top node, i erase all nodes that have a value greater than x... and append something like that at the end
    #when i reach the top, i iterate to the end, and make the final node the new top. Time complexity O(n*n) :(
    def x_partition(self,x):
        aux=self.head
        while(aux!=self.top):
            if(aux.data>=x):
                newNode=Node(aux.data)
                aux.data=aux.next.data
                aux.next=aux.next.next
                aux2=aux
                while(aux2.next!=None):
                    aux2=aux2.next
                aux2.next=newNode
            else:
                aux=aux.next
        while(aux.next!=None):
            aux=aux.next
        self.top=aux
        self.print_list()


    def x_partition_book_solution(self,x):
        aux=self.head
        list1=Single_linked_list()
        list2=Single_linked_list()
        while(aux!=None):
            if(aux.data>=x):
                list2.add_data(aux.data)
            else:
                list1.add_data(aux.data)
            aux=aux.next
        list1.top.next=list2.head
        list1.top=list2.top
        list1.print_list()
        #another similar solution is to make just list1 and add " > x " values, 
        #while erasing those values from the original list... and apending list1 to original list...

        








la_lista=Single_linked_list()
la_lista.add_data(3)
la_lista.add_data(5)
la_lista.add_data(8)
la_lista.add_data(5)
la_lista.add_data(10)
la_lista.add_data(2)
la_lista.add_data(1)
la_lista.print_list()
la_lista.x_partition(5)


# 3  5  8  5  10  2  1
# 3  5






