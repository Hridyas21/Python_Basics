#Polymorphism means "Many Forms"
#Overriding-->Same method name and parameters, but different implementation
class Animal:
    def speak(self):
        print("Some Generic Sound")
class Dog(Animal):
    def speak(self):
        print ("Bark")
class Cat(Animal):
    def speak(self):
        print("Meow")
        
a=Animal()
d=Dog()
c=Cat()
a.speak()
d.speak()
c.speak()  

#Overloading--> Same method name but different parameters
#In python operator overloading
class A:
    def __init__(self,vara,varb):
        self.a=vara
        self.b=varb
    
    def __add__(self,other): #__add__ is a magic method.eg: __sub__,__mul__,___div__,
        return self.a+other.a 
        #return self.a+other.a, self.b+other.b #will return the result as tuple
    
    

ob1=A(2,1)
ob2=A(3,4)
print(ob1+ob2)