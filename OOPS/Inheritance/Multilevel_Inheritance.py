class Father:
    def __init__(self,fname,fage):
        self.fathername=fname
        self.fatherage=fage

class Child1(Father):
    def __init__(self,ch1name,ch1age):
        self.child1name=ch1name 
        self.child1age=ch1age
        
class Child2(Child1):
    def __init__(self,ch2name,ch2age):
        self.child2name=ch2name 
        self.child2age=ch2age
    
c=Child1("Arun","23")
print()

