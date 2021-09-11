class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        ar=self.length*self.breadth
        print('area is:',ar)
    def parameter(self):
        peri=2*(self.length+self.breadth)
        print('perimeter is:',peri)

r1=Rectangle(10,20)
r1.area()
r1.parameter()
