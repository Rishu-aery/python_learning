# Input : test_str = ‘Gfg is best’
# Output : {‘Gfg’: 1, ‘is’: 1, ‘best’: 1}
#
# Input : test_str = ‘Gfg Gfg Gfg’
# Output : {‘Gfg’: 3}
# str = " pallavi is the good girl"
# a = {i:str.count(i) for i in str.split()}
# print(a)

# Python – Convert Snake case to Pascal case

# Input : geeks_for_geeks
# Output : GeeksforGeeks
#
# Input : left_index
# Output : leftIndex

# str = "geeks_for_geeks"
# a = "".join([ i for i in str.title().split("_")])
# print(a)

# str = "geeks_for_geeks"
# print(str.title().replace("_",""))


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

str = "This is a python language"
a = str.split(" ")
newlist = []   # sade kol i ch pya hoya this te asi otho na this di len find kr liye?hmmm
for i in a:
    n = len(i)
    if n%2 == 0 :
        newlist.append(i)
print(newlist)









