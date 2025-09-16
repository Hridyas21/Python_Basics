import re #module for regular expression

# pattern=r"Hello"

# message="Hello World"

# print(bool(re.match(pattern,message))) #it tries to match pattern at the beginning of message.
# #If the pattern matches at the start, re.match returns a match object (an instance of re.Match). 
# # #If it doesn't match at the start, it returns None

# pattern = r"\d"   # matches a single digit.matches any digit (0–9)
# message = "Room 42"

# match = re.search(pattern, message)
# if match:
#     print("Found:", match.group())  
    
# pattern=r"[A-Z0-9]"
# message="6developerhello42"
# print(bool(re.findall(pattern,message)))

# #enail validation
# #pattern=r"[A-Z0-9a-z]+@[a-zA-Z0-9]+\.(in|com|dev)$" #dollar symbol will checks till the last char.
# #pattern=r"[A-Z0-9a-z]+.[a-zA-Z0-9]+@[a-zA-Z0-9]+\.(in|com|dev)" #another email pattern
# pattern=r"[A-Z0-9a-z]{2,}@[a-zA-Z0-9]+\.(in|com|dev)" #{2,} specifies min 2 chars must be there. Then we can avoid "+" symbol
# email=input("Ebter your email: ")
# if re.match(pattern,email):
#     print("VALID")
# else:
#     print("Not Valid")
    
#password validation
pattern=r"(?=.*[a-z])(?=.*[A-Z])(?=.*\W).{8,}$" #?=.* represents "atleast" condition
#\W--> atleast one special character exists anywhere.
#{8,}--> Atleast 8 chars
password=input("Enter your password: ")
if re.match(pattern,password):
    print("VALID")
else:
    print("Not Valid")
  
