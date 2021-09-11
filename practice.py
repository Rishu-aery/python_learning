def sort(a):
    l=len(a)
    for i in range(0,l):
        for j in range(0,l-i-1):
            if a[j][1]>a[j+1][1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    return a

a=[]
for i in range(int(input())):
    name=input()
    score=float(input())
    a.append([name,score])
    print(a)
print(a)
sort(a)
print(a[1][0])


