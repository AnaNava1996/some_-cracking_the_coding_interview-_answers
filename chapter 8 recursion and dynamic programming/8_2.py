#whay is my input? what is my output?
#

#let's assume this
field=[[0,0,0,1,0,0],[0,0,1,0,0,0],[1,0,0,0,0,0],[0,0,0,0,0,0],[0,0,1,0,0,0],[0,0,0,0,0,0]]


''' cannot step in 1...
[0,0,0,1,0,0]
[0,0,0,1,0,0]
[0,0,0,0,0,0]
[0,0,0,0,0,0]
[0,0,1,0,0,0]
[0,0,0,0,0,0]
'''

path=set()

position=(0,0)
def try_down(position,path,r):
    if(position[0]==r-1):#if the robot have arrived at the bottom already
        return False
    elif((position[0]+1,position[1]) in path):#If the robot have been already in that point
        return False
    elif(field[position[0]+1][position[1]]==1):#if down is a 1
        return False
    else:
        return (position[0]+1,position[1])#the robot can go down

def try_right(position,path,c):
    if(position[1]==c-1):
        return False
    elif((position[0],position[1]+1) in path):
        return False
    elif(field[position[0]][position[1]+1]==1):
        return False
    else:
        return (position[0],position[1]+1)


def find_path(position,path,r,c):
    path.append(position)
    while((r-1,c-1)not in path):
        if(try_down(position,path,r)==False):#si no se puede ir abajo
            if(try_right(position,path,c)==False):#si no se puede ir a la derecha
                return False
            else:
                path=find_path(try_right(position,path,c),path,r,c)#se va a la derecha
        else:
            path=find_path(try_down(position,path,r),path,r,c)#se va a abajo
    print(path)
    return path

for i in field:
    print(i)

r=6
c=6
path=list()
find_path((0,0),path,r,c)
