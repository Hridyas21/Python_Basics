class Laptops:
    def Display(self): #'self' refers to the object calling this method
        print("Welcome")
        
lap1=Laptops()  #Creating an object of class Laptops
lap1.Display()  #Calls Display


class Laptops():
    def Specs(self,n,r):
        self.name=n
        self.RAM=r
        
lap1=Laptops() #object creation
lap2=Laptops()
lap1.Specs("HP","16 GB")
lap2.Specs("Dell","4 GB")
print(lap2.name)


#Constructor method
class Laptops():
    def __init__(self,n,r): #It is automatically called when you create a new object from a class.
        self.name=n
        self.RAM=r
    
    def Display(self):
        print(self)  
        print("Welcome")
        
lap1=Laptops("HP","16 GB") #created obj of class Laptops, the method will be automatically called, so can pass the arguments directly
lap2=Laptops("Dell","4 GB")

lap2.Display()
print(lap2.name)
