#Single Inheritance: A single child class inherits properties from a single parent class

class Vehicles: #Parent class
    def Details(self,m,mod):
        self.make=m
        self.model=mod
class Car(Vehicles): #Car is the child class, Car inherits Vehicles
    def __init__(self,c,p):
        self.color=c
        self.power=p
c1=Car("Red","151 Bhp")
c1.Details("2006","Kia Seltos")
print(c1.model,c1.make,c1.color)


#While using __init__ in both methods
#__init__() of the class related to the object will be called first.
#The parent class method have to be called then.

class Vehicles: #Parent class
    def __init__(self,m,mod):
        self.make=m
        self.model=mod
class Car(Vehicles): #Car is the child class, Car inherits Vehicles
    def __init__(self,c,p,m,model):
        self.color=c
        self.power=p
        super().__init__(m,model) #Super(): To call the method of parent class
c1=Car("Red","151 Bhp","2006","Kia Seltos")
print(c1.model,c1.make,c1.color,c1.power)
