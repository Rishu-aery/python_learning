lst=[['rish', 45.6],['egfd',15.6],['hgdj',34.6]]
print(lst)
l=len(lst)
for i in range(0,l):
    for j in range(0,l-i-1):
        if lst[j][1]>lst[j+1][1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
print(lst[1][0])

