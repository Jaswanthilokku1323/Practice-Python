class Grandpa:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)
class Dad(Grandpa):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)
class Me(Dad):
    def __init__(self,name,age,DOB):
        self.name=name
        self.age=age
        self.DOB=DOB
    def display(self):
        print(self.name,self.age,self.DOB)
GC=Me("Lohitha",16,"June")
GC.display()
