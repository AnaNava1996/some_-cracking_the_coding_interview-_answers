#actually.... it doesn't make much sense to do this in python
#that's why i'll put this on C... latter :)


def replacing(cad):
    count=0
    for i in cad:
        if(i==" "):
            count+=1
    print(count)
    cad=cad.replace(" ","%20",count)
    return cad


cad = "blabla blabla blasfasdas asdsd asdasd"
print(replacing(cad))







