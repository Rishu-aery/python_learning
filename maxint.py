# Program to return maximum integers of any combination of numbers
def max_int(num):
    l=sorted([i for i in str(num)])
    return int("".join([i for i in l[::-1]]))

num=input()
print(max_int(num))

# myTuple = ("John", "Peter", "Vicky")
#
# x = "#".join(myTuple)
#
# print(x)