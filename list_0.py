# Program to shift all zeros to end of list
l=[0,1,0,2,0,3,0]
print(l)
zero=[]
others=[]
for i in l:
    if i==0:
        zero.append(i)
    else:
        others.append(i)
print(others+zero)

