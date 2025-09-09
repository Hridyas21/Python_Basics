#Abstraction means hiding unnecessary details and showing only the important features to the user
#Abstraction is implemented using:Abstract methods and Abstarct classes
#built in abc module is used for this
#abc--> Absract Base Classes
#ABC--> lets us create abstract classes
#Implementation is in child class. Cannot create object for the parent class.

from abc import ABC,abstractmethod

class Parent(ABC): #Inherits from ABC, so its an absract class;Cannot create objectt for an abstract class.
    @abstractmethod #Used to mark methods that must be implemented in child classes

    def fun(self):
        pass        #This will be defined in the child class

class Child(Parent): #Class child is called the Concrete class
    def Display(self):
        print("HELLO")
    def fun(self):
        print("Abstract method implementation")
        
obj=Child()
obj.Display()
obj.fun()

#Another example
from abc import ABC,abstractmethod
class BankPayment(ABC):
    @abstractmethod
    def payment(self):
        pass
class NetBanking(BankPayment):
   
    def payment(self):
        print("Hello Everyone")

ob2=NetBanking()
ob2.payment()