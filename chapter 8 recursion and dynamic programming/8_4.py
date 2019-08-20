#questions: how do i represent the empty value?


def function(the_set):
    set_of_sets=set()
    try:
        if(len(the_set)==1):     
            set_of_sets.add(the_set)
        elif(len(the_set)!=0):
            set_of_sets.add(the_set)
            for i in range(0,len(the_set)):
                set_of_sets.update( function(the_set[0:i]+the_set[i+1:] ))
    except:
        print("loquesea")
    return set_of_sets


the_set=(1,2,3,4,5,6)
print(function(the_set))

