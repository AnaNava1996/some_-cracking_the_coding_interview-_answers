#Given two strings, write a method to decide if one is a permutation of the other


def is_it_a_permutation(a,b):
    dic=dict()
    for letter in a:
        if(letter in dic):
            dic[letter]+=1
        else:
            dic[letter]=1
    print(dic)
    for letter in b:
        if(letter in dic):
            dic[letter]-=1
        else:
            print("oh no")
            return False
    print(dic)
    for value in dic:
        if(dic[value]!=0):
            print(value)
            return False
    return True


cad1="holacooomoestas"
cad2="holacomoestasasasasasass"

print(is_it_a_permutation(cad1,cad2))





























