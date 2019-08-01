def con_espacio_extra(cad):#complejidad O(n) en tiempo donde n es el lardo de la palabra
    lista=[0]*265           #complejidad 256+n en espacio?
    for i in cad:
        lista[ord(i)]=lista[ord(i)]+1
    for i in range(0,len(lista)):
        if(lista[i]>1):
            return False
    return True

def sin_espacio_extra(cad): #complejidad ?
    for i in range(0,len(cad)-1):
        for j in range(i+1, len(cad)):
            print("si "+ cad[i]+" = "+cad[j])
            if(cad[i]==cad[j]):
                return False
    return True

def sin_espacio_extra_2(cad):
    cad=sorted(cad)
    for i in range(0,len(cad)-1):
        if(cad[i]==cad[i+1]):
            return False
    return True

cad="adcidos"

print(con_espacio_extra(cad))
print(sin_espacio_extra(cad))
print(sin_espacio_extra_2(cad))























