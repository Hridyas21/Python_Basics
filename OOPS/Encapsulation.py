#Encapsulation means hiding data inside a class and only allowing access to it through methods.
#Wrapping up of data (variables) and code (methods) into a single unit called a class, and restricting direct access to some of the object's components.
# Python has 3 main access levels. These help implement encapsulation.

#Public-That usually we do
class Private:
    def sal(self,s):
        self.salary=s #private variable
        print("salary is: ",self.salary) 
    
s=Private()
s.sal("50000")

#Private
#Accessed only from its class
# can't access it directly from outside the class.
#double underscore __ to make something private.
#In python there is no true private variable like java or C++.

class Private:
    def sal(self):
        self.__salary=49999 #private variable
        #return self.__salary
        print("salary is: ",self.__salary) 
    
s=Private()
s.sal()  # calls the sal() method, which sets the private variable and prints
#print("salary is:",s.sal())
  
#Protected
#Can be accessed from it's class only
#Single underscore
#Can access directly, No such concept in python. Since it is not a fully object oriented programming language.