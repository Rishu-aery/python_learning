time=input('Enter time in HH:MM format:')
hour,mins=[int(i) for i in time.split(':')]

print('it is',hour,'hours and',mins,'minutes')
b_tax=((mins/60)+hour)*30
a_tax=b_tax+(b_tax*0.15)
print('Charge per hour is $30')
print('Before tax:',b_tax)
print('After tax:',a_tax)