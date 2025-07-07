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
result=num1+num2
print(result)