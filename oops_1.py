class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def explain(self):
        return f"Name is {self.fname} {self.lname}"
    @property
    def email(self):
        return f"{self.fname}.{self.lname}@gmail.com"
    @email.setter
    def email(self,string):
        print(string)
        names=string.split('@')[0]
        self.fname=names.split('.')[0]
        self.lname = names.split('.')[1]

Rishabh_aery=Employee('Rishabh','aery')
print(Rishabh_aery.explain())
print(Rishabh_aery.email)
Rishabh_aery.fname="Akshit"
print(Rishabh_aery.email)
Rishabh_aery.email="Us.india@gmail.com"
print(Rishabh_aery.email)

