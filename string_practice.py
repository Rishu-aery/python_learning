# Input : test_str = ‘Gfg is best’
# Output : {‘Gfg’: 1, ‘is’: 1, ‘best’: 1}
#
# Input : test_str = ‘Gfg Gfg Gfg’
# Output : {‘Gfg’: 3}

# test_str ='Gfg is best'
# new={key:test_str.count(key) for key in test_str.split()}
# print(new)


# Python – Convert Snake case to Pascal case

# Input : geeks_for_geeks
# Output : GeeksforGeeks
#
# Input : left_index
# Output : leftIndex

# str='geeks_for_geeks'
# res=str.title().replace("_",'')
# print(res)

'''Python program to print even length words in a string'''

# Input: s = "This is a python language"
# Output: This
#         is
#         python
#         language
#
# Input: s = "i am muskan"
# Output: am
#         muskan

#
# s = "This is a python language"
# a=s.split()
# for i in a:
#     if len(i) %2==0:
#         print(i)





'''Find words which are greater than given length k'''

# Examples:
#
# Input : str = "hello geeks for geeks
#           is computer science portal"
#         k = 4
# Output : hello geeks geeks computer
#          science portal
# Explanation : The output is list of all
# words that are of length more than k.
#
# Input : str = "string is fun in python"
#         k = 3
# Output : string python

# str = "string is fun in python"
# k= int(input("enter k:"))
# a=str.split()
# new_list=[]
# for i in a:
#     if len(i)>k:
#         new_list.append(i)
# print(" ".join(new_list))


'''Python | Check if a given string is binary string or not'''

# Examples:
#
# Input: str = "01010101010"
# Output: Yes
#
# Input: str = "geeks101"
# Output: No

# str = "01010101011"
# n=len(str)
# for i in range(0,n):
#     if str[i]=='1' or str[i]=='0':
#         continue
#     else:
#         print("String is NOT binary")
#         break
# if i==(n-1) and str[i]=='1' or str[i]=='0':
#     print('YES')

'''Python program to find uncommon words from two Strings'''

# Examples:
#
# Input : A = "Geeks for Geeks"
#         B = "Learning from Geeks for Geeks"
# Output : ['Learning', 'from']
#
# Input : A = "apple banana mango"
#         B = "banana fruits mango"
# Output : ['apple', 'fruits']

# str1 = "apple banana mango"
# str2 = "banana fruits mango"
# str1_list= str1.split()
# str2_list= str2.split()
# new_list=[]
# for i in str2_list:
#     if i not in str1_list:
#         new_list.append(i)
# for j in str1_list:
#     if j not in str2_list:
#         new_list.append(j)
#
# print(new_list)


'''Python – Replace duplicate Occurrence in String'''

# The original string is :    Gfg is best . Gfg also has Classes now. Classes help understand better .
# The string after replacing :    Gfg is best . It also has Classes now. They help understand better .

str = 'Gfg is best . Gfg also has Classes now. Classes help understand better .'
a= str.split()
b=set(a)
print(b)
print(' '.join(a))


