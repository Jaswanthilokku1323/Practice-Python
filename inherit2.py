class a:
    def t(self):
        print("Parent")
class b:
    def t1(self):
        print("Parent1")
class c(b,a):
    def t2(self):
        print("child")
obj=c()
obj.t2()
obj.t()
obj.t1()
print(issubclass(c,b))
print(issubclass(a,b))
print(issubclass(c,a))
print(isinstance(obj,c))
#method overriding
class Father:
    def transport(self):
        print("Bike")
class Son(Father):
    def transport(self):
        #calling parent class
        Father.transport(self)
        print("car")
obj=Son()
obj.transport()
class p1:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Viggie")
class p2(p1):
    def __init__(self,age):
        super().__init__("ok")
        self.age=age

    def display(self):

        print("Yes")
        print(self.age)
class c(p2):
    def __init__(self,id):
        super().__init__("Done")
        self.id=id
    def display(self):
        print("Perfect")
        print(self.id)
obj=p2(34)
obj1=c(72)
obj.display()
obj1.display()
