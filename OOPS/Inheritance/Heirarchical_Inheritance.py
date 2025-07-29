#Simple program (Basic)

class Father:
    def Father_Details(self,fname,fage,fsalary,feye):
        self.fathername=fname
        self.fatherage=fage
        self.fathersalary=fsalary
        self.fathereyecolor=feye
        
class Child1(Father):
    def Child1_Details(self,ch1name,ch1age,ch1salary,ch1eye):
        self.child1name=ch1name 
        self.child1age=ch1age
        self.child1salary=ch1salary 
        self.child1eyecolor=ch1eye
        
    def Display1(self):
        print("====Child1 Details====")
        print("Name: ",self.child1name)
        print("Age: ",self.child1age)
        print("Eyecolor: ",self.child1eyecolor)
        print("Salary: ",self.child1salary)
        print("Father's Name:", self.fathername)
        print("Father's Age:", self.fatherage)
        print("Father's Salary:", self.fathersalary)
        
class Child2(Father):
    def Child2_Details(self,ch2name,ch2age,ch2salary,ch2eye):
        self.child2name=ch2name 
        self.child2age=ch2age
        self.child2salary=ch2salary 
        self.child2eyecolor=ch2eye
        
    def Display2(self):
        print("====Child2 Details====")
        print("Name: ",self.child2name)
        print("Age: ",self.child2age)
        print("Eyecolor: ",self.child2eyecolor)
        print("Father's Name:", self.fathername)
        print("Father's Age:", self.fatherage)
        print("Father's Salary:", self.fathersalary)
c1=Child1()
c2=Child2()

c1.Child1_Details("Arun","23","34000","Black")
c1.Father_Details("John","56","45000","brown")

c2.Child2_Details("Amal","20","30000","Brown")
c2.Father_Details("John","56","45000","brown")

c1.Display1()
c2.Display2()

#using __init__ method explicitly called
class Father:
    def __init__(self,fname,fage,fsalary,feye):
        self.fathername=fname
        self.fatherage=fage
        self.fathersalary=fsalary
        self.fathereyecolor=feye
        
class Child1(Father):
    def __init__(self,ch1name,ch1age,ch1salary,ch1eye,fname,fage,fsalary,feye):
        self.child1name=ch1name 
        self.child1age=ch1age
        self.child1salary=ch1salary 
        self.child1eyecolor=ch1eye
        Father.__init__(self,fname,fage,fsalary,feye)
        
    def Display1(self):
        print("====Child1 Details====")
        print("Name: ",self.child1name)
        print("Age: ",self.child1age)
        print("Eyecolor: ",self.child1eyecolor)
        print("Salary: ",self.child1salary)
        print("Father's Name:", self.fathername)
        print("Father's Age:", self.fatherage)
        print("Father's Eyecolor: ",self.fathereyecolor)
        print("Father's Salary:", self.fathersalary)
        
class Child2(Father):
    def __init__(self,ch2name,ch2age,ch2salary,ch2eye,fname,fage,fsalary,feye):
        self.child2name=ch2name 
        self.child2age=ch2age
        self.child2salary=ch2salary 
        self.child2eyecolor=ch2eye
        Father.__init__(self,fname,fage,fsalary,feye)
        
    def Display2(self):
        print("====Child2 Details====")
        print("Name: ",self.child2name)
        print("Age: ",self.child2age)
        print("Eyecolor: ",self.child2eyecolor)
        print("Father's Name:", self.fathername)
        print("Father's Age:", self.fatherage)
        print("Father's Eyecolor: ",self.fathereyecolor)
        print("Father's Salary:", self.fathersalary)
        
c1=Child1("Arun","23","34000","Black","John","56","45000","brown")
c2=Child2("Amal","20","30000","Brown","John","56","45000","brown")

c1.Display1()
c2.Display2()


#__init__ method called using super()
class Father:
    def __init__(self,fname,fage,fsalary,feye):
        self.fathername=fname
        self.fatherage=fage
        self.fathersalary=fsalary
        self.fathereyecolor=feye
        print("Father is called")
        
class Child1(Father):
    def __init__(self,ch1name,ch1age,ch1salary,ch1eye,fname,fage,fsalary,feye):
        self.child1name=ch1name 
        self.child1age=ch1age
        self.child1salary=ch1salary 
        self.child1eyecolor=ch1eye
        print("Chikd1 is called")
        super().__init__(fname,fage,fsalary,feye)
        
    def Display1(self):
        print("====Child1 Details====")
        print("Name: ",self.child1name)
        print("Age: ",self.child1age)
        print("Eyecolor: ",self.child1eyecolor)
        print("Salary: ",self.child1salary)
        print("Father's Name:", self.fathername)
        print("Father's Age:", self.fatherage)
        print("Father's Eyecolor: ",self.fathereyecolor)
        print("Father's Salary:", self.fathersalary)
        
class Child2(Father):
    def __init__(self,ch2name,ch2age,ch2salary,ch2eye,fname,fage,fsalary,feye):
        self.child2name=ch2name 
        self.child2age=ch2age
        self.child2salary=ch2salary 
        self.child2eyecolor=ch2eye
        print("Child2 is called")
        super().__init__(fname,fage,fsalary,feye)
        
    def Display2(self):
        print("====Child2 Details====")
        print("Name: ",self.child2name)
        print("Age: ",self.child2age)
        print("Eyecolor: ",self.child2eyecolor)
        print("Father's Name:", self.fathername)
        print("Father's Age:", self.fatherage)
        print("Father's Eyecolor: ",self.fathereyecolor)
        print("Father's Salary:", self.fathersalary)
        
c1=Child1("Arun","23","34000","Black","John","56","45000","brown")
c2=Child2("Amal","20","30000","Brown","John","56","45000","brown")

c1.Display1()
c2.Display2()