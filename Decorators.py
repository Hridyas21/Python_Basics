# # Decorators are a powerful feature in Python that allow you to modify the behavior of a function (or class) without changing its code.
# # Think of them as wrappers that add extra functionality to existing functions.

# # A simple decorator function
# def decorator(func):
  
#     def wrapper():
#         print("Before calling the function.")
#         func()
#         print("After calling the function.")
#     return wrapper

# # Applying the decorator to a function
# @decorator

# def greet():
#     print("Hello, World!")

# greet()


# #Example
# def Dec(fun): #Decorator definition
#     def wrapper(msg): #Inner wrapper function (nested function),any name can be given ;wrapper is not a keyword
#         a=msg.upper()
#         fun(a)    # Call the original function with modified message
#     return wrapper


# @Dec 
# def Greetings(m): #Function to be decorated(modified)
#     print(m)
    
# Greetings("Hello Developers..")

#Subtraction

def dec(fun):
    def wrapper(a,b):
        if a<b:
            a,b=b,a
        fun(a,b)
    return wrapper

@dec
def Subtraction(a,b):
    print(a-b)
    
Subtraction(2,10)