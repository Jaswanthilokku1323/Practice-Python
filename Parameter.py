'''class Emp:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print(self.id,self.name)
emp1=Emp("Lucky",71)
emp2=Emp("Sunny",73)
emp1.display()
emp2.display()'''
class emp:
    def __init__(self,name):
        print("constructor with parameters")
        self.name=name
    def show(self):
        print("Lokku",self.name)
e1=emp("Jaswanthi")
e1.show()