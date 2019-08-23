#special cases: multiply by 0

def multiply(n,count,m):#recursive
    if(m==0):
        return count
    else:
        count=count+n
        m=m-1
        return multiply(n,count,m)

def multiply2(n,m):#also recursive but with two parameters
    if(n==0 or m==0):
        return 0
    elif(m==1):
        return n
    else:
        count=n
        count=count+multiply2(n,m-1)
        return count

def non_recursive_way(n,m):#iterating
    temp=0
    for i in range(0,m):
        temp=temp+n
    return temp


print(multiply(0,0,2))
print(multiply(2,0,0))
print(multiply(20,0,4))
print(multiply(20,0,1))
print(multiply(1,0,4))

print(multiply2(0,2))
print(multiply2(2,0))
print(multiply2(20,4))
print(multiply2(20,1))
print(multiply2(1,4))

print(non_recursive_way(0,2))
print(non_recursive_way(2,0))
print(non_recursive_way(20,4))
print(non_recursive_way(20,1))
print(non_recursive_way(1,4))



