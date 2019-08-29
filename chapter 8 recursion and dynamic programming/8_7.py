def permutations(the_string):
    if(len(the_string)==1):
        alist=[]
        alist.append(the_string)
        return alist
    elif(len(the_string)==2):
        alist=[]
        alist.append(the_string)
        alist.append(the_string[1]+the_string[0])
        return alist
    elif(len(the_string)==3):
        alist=[]
        alist.append(the_string[0]+the_string[1]+the_string[2])
        alist.append(the_string[0]+the_string[2]+the_string[1])
        alist.append(the_string[2]+the_string[1]+the_string[0])
        alist.append(the_string[2]+the_string[0]+the_string[1])
        alist.append(the_string[1]+the_string[0]+the_string[2])
        alist.append(the_string[1]+the_string[2]+the_string[0])
        return alist
    else:
        alist=[]
        for i in range(0,len(the_string)):
            temp_list=permutations(the_string[0:i]+the_string[i+1:])
            for j in temp_list:
                for k in range(0,len(j)-1):
                    if((j[:k]+the_string[i]+j[k:]) not in alist):
                        alist.append(j[:k]+the_string[i]+j[k:])
                if((j+the_string[i]) not in alist):
                    alist.append(j+the_string[i])
        return alist


the_string="12345"
print(permutations(the_string))
print(len(permutations(the_string)))
'''
123     132     213     231     312     321

4123
1423
1243
1234

'''
                
