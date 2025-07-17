c=0
def sample():
    d=c+1
    print(d)
sample()

c=0
def sample():
    global c
    c=c+1 #C is being changed sp "c" should be declared as the global variable
    print(c)
sample()

