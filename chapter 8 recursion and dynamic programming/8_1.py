#what kind of input? none, 0, 1, negative... etc....
#is it different 1-2-1 than 2-1-1 ? 
 
    
def recursive_function(n,x):
    count=0
    for i in x:
        if(n-i==0):
            count+=1
        elif(n-i>0):
            count += recursive_function(n-i,x)
    return count




x=[1,2,3]   #possible hops 
n=5         #number of steps    
print(recursive_function(n,x))




