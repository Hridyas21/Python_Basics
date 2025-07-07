age=int(input("Enter your age :"))
if(age>=18):
    print("ELIGIBLE FOR VOTING..")
else:
    print("NOT ELIGIBLE FOR VOTING..!!")

#even or odd
num=int(input("Enter a number:"))
if(num%2==0):
    print(num, "is even")
else:
    print(num, "is odd")
    
leap year
year=int(input("Enter the year:"))
if (year%4==0 and year%100!=0 or year%40==0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
    
nested if

year=int(input("Enter the year:"))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")
    
payment_status=False #If given anything instaed of True or False it will check for NONE; If None -->True
mark=int(input("Enter the marks:"))
if payment_status:
    if (mark>60):
        print("Eligible for appearing for the exam")
    else:
        print("Not eligible for appeaeing for the exam")
else:
    print("Complete the due")
    
#if-elif
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
print("Please choose your option:")
print("\n1.Addition\n2.Subtraction\n3.Division\n4.Multiplication\n")
ch=int(input("Enter your choice:"))
if(ch==1):
    res=num1+num2
    print(res)

elif(ch==2):
    res=num1-num2
    print(res)
elif(ch==3):
    res=num1/num2
    print(res)

elif(ch==4):
    res=num1*num2
    print(res)

else:
    print("INVALID CHOICE!!")


num=int(input("Enter a number:"))
if(num<0):
    print(num, "is negative number")
elif(num>0):
    print(num, "is positive number")
else:
    print("zero")
    

day=int(input("Enter the day 1-7:"))
if(day==1):
    print("Sunday")
elif(day==2):
    print("Monday")
elif(day==3):
    print("Tuesday")
elif(day==4):
    print("Wednesday")
elif(day==5):
    print("Thursday") 
elif(day==6):
    print("Friday") 
elif(day==7):
    print("Saturday")
else:
    print("INVALID!!")

age=int(input("Enter your age:"))
if(age<13):
    print("Child")
elif(age<20):
    print("Teenager")
elif(age<60):
    print("Adult")
else:
    print("Senior citizen")