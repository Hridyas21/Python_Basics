 #Simple program without __init__
 
class Father:
    def Father_Details(self,n,a,s):
        self.fathername=n
        self.fatherage=a 
        self.fathersalary=s
    
class Mother:
    def Mother_Details(self,n,a,s):
        self.mothername=n
        self.motherage=a 
        self.mothersalary=s
        
class Child(Father,Mother):
    def Bio(self,n,a):
        self.name=n
        self.age=a

    def Display(self):
        print("Name: ",c.name)
        print("Age: ",c.age)
        print("Father's Name:",c.fathername)
        print("Mother's Name: ",c.mothername)
        print("Father's Salary: ",c.fathersalary)
        print("Mother's Salary: ",c.mothersalary)

c=Child()
c.Father_Details("John","56","100000")
c.Mother_Details("Jain","46","200000")
c.Bio("Arun","23")
c.Display()

#Using __init__ method
#child's __init__ method is called automatically(the class which created object)
#__init__ of parent classes should be called explicitly. 
#It will be called in the order of inherited, child(parent1,parent2)
#__init__ of parent1 will be called first then of parent2
#super() is not used since called using class name

class Father:

    def __init__(self,n,a,s):
        self.fathername=n
        self.fatherage=a 
        self.fathersalary=s
    
class Mother:
    def __init__(self,n,a,s):
        self.mothername=n
        self.motherage=a 
        self.mothersalary=s
        
class Child(Father,Mother):
    def __init__(self,n,a,fname,fage,fsalary,mname,mage,msalary):
 
        self.name=n
        self.age=a
        Father.__init__(self,fname,fage,fsalary) #calling __init__ method using class name
        Mother.__init__(self,mname,mage,msalary)
    
    def Display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Father's Name:",self.fathername)
        print("Father's Salary: ",self.fathersalary)
        print("Mother's Name: ",self.mothername)
        print("Mother's Salary: ",self.mothersalary)
        
c=Child("Arun","23","John","56","20000","Jain","45","25000")
c.Display()


#Using super()
#The child class super() calls the __init__ of parent class inherited first(father)
#In Father class super() calls the __init__ of Mother

class Father:

    def __init__(self,n,a,s,mname,mage,msalary):
        self.fathername=n
        self.fatherage=a 
        self.fathersalary=s
        super().__init__(mname,mage,msalary)
    
class Mother:
    def __init__(self,n,a,s):
        self.mothername=n
        self.motherage=a 
        self.mothersalary=s
        
class Child(Father,Mother):
    def __init__(self,n,a,fname,fage,fsalary,mname,mage,msalary):
        
        self.name=n
        self.age=a
        super().__init__(fname,fage,fsalary,mname,mage,msalary,)
        
    def Display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Father's Name:",self.fathername)
        print("Father's Salary: ",self.fathersalary)
        print("Mother's Name: ",self.mothername)
        print("Mother's Salary: ",self.mothersalary)
        
c=Child("Arun","23","John","56","20000","Jain","45","25000")
c.Display()

