# Program to add whitespaces in string
str='HelloWorld'
a=[]
for i in str:
    if i.isupper():
        a.append(' '+i)
    else:
        a.append(i)
print(''.join(a).strip())
