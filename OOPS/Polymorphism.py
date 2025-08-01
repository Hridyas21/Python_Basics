#Polymorphism means "Many Forms"
#Overriding-->Same method name and parameters, but different implementation
class Animal:
    def speak(self):
        print("Meow")
class Dog:
    def speak(self):
        print("Bark")
        
a=Animal()
d=Dog()
a.speak()
d.speak()
     
#Overloading--> Same method name but different parameters