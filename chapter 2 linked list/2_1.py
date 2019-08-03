def eliminar_rep_con_extra_space(cad):
    newcad=""
    for i in range(0,len(cad)):
        if(cad[i] in newcad):
            pass
        else:
            newcad=newcad+cad[i]
            print(newcad)
    return newcad

def eliminar_sin_extra_space(cad):
    index=0
    n=len(cad)-1
    while(index<n-1):
        index2=index+1
        while(index2<n+1):
            if(cad[index]==cad[index2]):
                n-=1
                cad=cad[:index2]+cad[index2+1:]
            else:
                index2+=1
        index+=1
    print(cad)
    return cad    

cad="acidoooacdi"
cad=eliminar_rep_con_extra_space(cad)
cad="acidoooacdi"
cad=eliminar_sin_extra_space(cad)
