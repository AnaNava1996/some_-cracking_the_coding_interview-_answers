#are the values in the array always integers?
#if there is not a magic index, what do you whant to return?
#are there any repeated numbers?...
def search_handler(alist):
    num=len(alist)//2
    return search(alist,num)


def search(alist,num):
    index=(len(alist)//2)
    if(len(alist)==1):
        if(alist[0]==num):
            return num
        else:
            return False
    else:
        if(alist[index]==num):
            return num
        else:
            if(alist[index]<num):
                return search(alist[index+1:],num+(len(alist[index+1:])//2)+1)
            else:
                return search(alist[:index],num-(len(alist[:index])-len(alist[:index])//2))


#alist=[-20,1,2,4,5,6,7]
alist=[-40,-20,-1,1,2,3,5,7,9,12,13]
print(search_handler(alist))
        
