
#recursivamente regresa si se encuentra o no
def binary_search(alist,search_num):
    n=len(alist)
    index=n//2
    if(alist[index]==search_num):
        return True
    elif(n>1):
        if(search_num<alist[index]):
            return binary_search(alist[:index],search_num)
        else:
            return binary_search(alist[index:],search_num)
    else:
        return False
#se podrá regresar el indice si se hace recursivo?



#      0 1 2 3 4 5 6 7 8  9 10 11 12 13 14
alist=[1,2,3,4,5,6,7,8,9,12,14,16,19,20,30]#len=15    15//2=7   
print(binary_search(alist,13))


