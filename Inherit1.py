class Dog:
    def __init__(self,petname):
        self.name=petname
    def display(self):
        print(self.name)
class Puppy(Dog):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)
a=Puppy("Choco",3)
a.display()


