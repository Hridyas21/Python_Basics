#Encapsulation means hiding data inside a class and only allowing access to it through methods.
#Python has 3 main access levels. These help implement encapsulation.

#Public-That usually we do
class Private:
    def sal(self,s):
        self.salary=s #private variable
        #return self.__salary
        print("salary is: ",self.salary) 
    
s=Private()
s.sal("50000")

#Private
# can't access it directly from outside the class.
#double underscore __ to make something private.

class Private:
    def sal(self):
        self.__salary=49999 #private variable
        #return self.__salary
        print("salary is: ",self.__salary) 
    
s=Private()
s.sal()  # calls the sal() method, which sets the private variable and prints
#print("salary is:",s.sal())
  
#Protected
     