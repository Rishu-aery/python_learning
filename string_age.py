# Program to check age and sum if age is less than 20

import re
str='sachin:25, rajat:22, rishabh:13'
print(str)
a=re.split(':|,',str)
sum=0
size=len(a)
i=1
for j in a:
    if i%2==0:
        if int(j) > 20:
            sum += int(j);
    i+=1
print(sum)





# lst=['12','14','13','9']
# for i in lst:
#     if int(i) >10:
#         print(i)
#     else:
#         print('hi')


