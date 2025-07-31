from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('Rohit', 21)
person2 = Person.fromBirthYear('Abin', 2002)

print(person1.age)
print(person2.age)

# print the result
print(Person.isAdult(person2.age))


#Static Method
class Cake:
    @staticmethod
    def is_sweet():
        print("All cakes are sweet")
c=Cake() #In staticmethod object creation is not mandatory.
c.is_sweet() #Can call directly using classs name

#Class Method
class Cake():
    Bakery_name="Sweet Cakes"
    
    @classmethod
    def change_name(cls,new_name):
        cls.Bakery_name=new_name
        
c=Cake()   
Cake.change_name("Yummy Bakes")
print(Cake.Bakery_name) 
        