def funargs(a,*args,**kwargs):
    print(type(args))     #The argument of *args is passed as a tuple
    print(a)
    for i in args[::]:
        print(f'My name is: {i}')
    print()
    for key,value in kwargs.items():
        print(f'first name: {key}')
        print(f'Last name: {value}')


a=30
name_list=['pallavi','Rishabh','Rajat','Harry','Akshit']
d1={'Rishabh':'aery','Pallavi':'rampal','Rajat':'sharma'}
funargs(a,*name_list,**d1)

"""We can also pass normal variable with *args, but we cannot pass normal variable after the
 *args 
 The convention is: def f1(normal_variable,*args,**kwargs)
 NOTE- if we change this convention the program will generate an error..
 
 the argument passed as a **kwargs must be dictionory.
 
 
  *args and **kwargs are optional arguments..
  the program does not through an error if we don't pass the *args and **kwargs"""