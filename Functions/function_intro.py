def fun():
    print("Hello..")
fun() #function call


def greet(name):
    print("Hello",name)
greet("Hridya")
greet("Kichu")
greet("Devu")

def fact(num):
    pass #placeholder, we can leave this without completeing
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