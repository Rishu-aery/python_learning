from units import unit
metre=unit('m')
name=input("Enter name of the room:")
l=int(input('Enter length(in meters):'))
w=int(input('Enter width(in meters):'))
ar=l*w
print("Area of your",name," room will be:",metre(ar))
cost=ar*425  #  $425 is given cost of per metre square
currency='${:,.2f}'.format(cost)
print('The approximate cost of the room is:',currency)