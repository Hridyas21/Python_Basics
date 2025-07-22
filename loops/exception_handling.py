a,b=10,0
try: #Code that might raise an exception

    c=a/b
    print(c)
#except Exception: #Code to handle the exception

except Exception as e: #catches the exception, and stores the error message in variable e.
    print("Please enter a valid number!")
    #print("Please enter a valid number!",e)
    
else:
    print("No errors found")
    
finally: #Always works 
  print("Program executed")

    
a,b=10,0
try: #Code that might raise an exception

    c=a/j
    #c=a/b
    print(c)
except ZeroDivisionError:
    print("enter a valid number")
except NameError:
    print("Value not found")

