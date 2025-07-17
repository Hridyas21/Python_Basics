def fun():
    #name="Hridya"  #If given like this, Always print "Hello Hridya"
    print("Hello..")
fun() #function call


def greet(name):
    print("Hello",name)
greet("Hridya")
greet("Kichu")
greet("Devu")

def fact(num):
    pass #placeholder, we can leave this without completing
fact(5)

#Factorial of a number using function
def factorial(num):
    f=count=1
    while(count<=num):
        f=f*count
        count=count+1
    print(f)
factorial(5)

#even or odd
def even_or_odd(num):
    if(num%2==0):
        print("Even number")
    else:
        print("Odd Number")
even_or_odd(4)
even_or_odd(1)

def is_positive(num):
    if(num>=0):
        print("Positive")
    else:
        print("Negative")
print(is_positive(-3)) #This will result "None" since there is no return type



def is_positive(num):
    if(num>=0):
        return True
    else:
        return False

def even_or_odd(num):
    if(num%2==0):
        print(num, "is even")
    else:
        print(num, "is odd")
   
num=int(input("Enter the number:"))     
if is_positive(num):
    even_or_odd(num)
else:
    print("Number is negative")

def add(a,b):
    return a+b #return statement immediately ends the function
    #print(a+b)--->This will not print
#add(1,2) --->will not print since print is not given
print(add(1,2))#--->3


#average of numbers in a list
def total(numbers):
    sum=0 
    for num in numbers:
        sum=sum+num
    return sum

list1=[10,20,30,40]
s=total(list1)
avg=s/len(list1)
print(avg)

#Positional arguments
def add(a,b):
    sum=a+b
    print(sum)
add(a=10,b=20) #positional arguments 
#add(10) ---> gives positional arguments error
#or
#def add(a) --->gives positional arguments error since only one parameter is defines and passing 2 arguments


def add(*n): # *args (for non keyword arguments) can take multiple arguments;"args" is not a keyword
    print(n)
add(1,2,3)

def greet(**student): # **kargs used for keyword arguments
    print(f"Hello {student["name"]} you are {student["age"]} years old") #name and age are not directly defined , they are in dictionary "student"
greet(name="Hridya",age=21)

def sample(a,b):
    return a,b
a,b=sample(1,2) #unpacking the tuple into 2 variables; a=1,b=2
print(a,b) 