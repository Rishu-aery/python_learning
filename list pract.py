import numpy
lst = [10,15,5,6,7,8,9,10,8,6,4,9]
# result1 = numpy.prod(lst)
# print(result1)

# Python program to find second largest number in a list
# n=int(input('enter n:'))
# lst.sort()
#
#
# def Nmaxelements(list1, N):
#     final_list = []
#
#     for i in range(0, N):
#         max1 = 0
#
#         for j in range(len(list1)):
#             if list1[j] > max1:
#                 max1 = list1[j];
#
#         list1.remove(max1);
#         final_list.append(max1)
#
#     print(final_list)
#
#
# # Driver code
# list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10]
# N = 2

# Calling the function
# Nmaxelements(list1, N)




start = int(input('enter the starting number:' ))
end = int(input('enter the end number:'))
while(start!=end):
    if start % 2 == 0 :
        print(start)
    elif start%2!=0:
        print(start)
    start = start + 1