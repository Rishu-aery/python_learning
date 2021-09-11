def getdate():
    import datetime
    return datetime.datetime.now()


def take():
    if l == 1:
        with open(x + '_food', 'a') as f:
            food = input('type here:\n')
            f.write(str(getdate()) + ':')
            f.write(food)
            f.write('\n')
            print('successfully written')

    elif l == 2:
        with open(x + '_ex', 'a') as f:
            food = input('type here:\n')
            f.write(str(getdate()) + ':')
            f.write(food)
            f.write('\n')
            print('successfully written')


def retrieve():
    if l == 1:
        with open(x + '_food') as f:
            a = f.read()
            print(a)
    elif l == 2:
        with open(x + '_ex') as f:
            a = f.read()
            print(a)

"""MAIN PROGRAM...."""

print('HEALTH MANAGEMENT SYSTEM')
a = int(input('enter 1 for log and 2 for retrieve:'))
if a!=1 and a!=2:
    print("invalid number")
else:
    x = input("enter name:")
    print("details of name you enter", x)
    print("enter the number 1 for food and 2 for exercise")
    l = int(input(""))
    if a == 1:
        take()
    elif a == 2:
        retrieve()
