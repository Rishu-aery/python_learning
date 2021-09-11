'''Program to capitalize a main string'''

# main_str=["my","name","is","rishabh","aery"]
# minor_str=["an","is","of"]
#
# for main in main_str:
#     if main not in minor_str:
#         print(main.capitalize(),end=" ")
#     else:
#         print(main,end=" ")
def title_case(title,minor):
    l=title.split()
    print(l)
    return' '.join([i.lower() if i.lower()in minor else i.capitalize() for i in l])


title=input()
minor='a an of is the'
print(title_case(title,minor))













