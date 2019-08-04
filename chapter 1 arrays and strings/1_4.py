

#I think I would ask if the spaces count for the palyndrome
# if it doesnt...


def is_a_permutation(cad):
    if(cad==None):
        print("...the fuck did you entered?")
        return False
    elif(len(cad)==0):
        return False
    elif(len(cad)==1):
        return True
    else:
        dic=dict()
        for i in cad:
            if(i!=' '):
                if(i in dic):
                    dic[i]+=1
                else:
                    dic[i]=1
        count=0
        for i in dic:
            if(dic[i]%2==1):
                count+=1
        if(count!=1):
            return False
        else:
            return True



cad="tact coa"#it's a permutation of anita lava la tina wich is a palyndrome
print(is_a_permutation(cad))

#I would also ask what kind of inputs i should expect ?
#what happends with upper case and stuff... like is C equal to c ?... if that's the case it would be good to convert those letters... 









