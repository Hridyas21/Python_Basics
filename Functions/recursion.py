# #A function calls itself is called Recursion

# #Factorial using recursion

# def fact(num):
#     if(num==1 or num==0):
#         return 1
#     else:
#         return num*fact(num-1)
# print(fact(5))

#sum of natural numbers
def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
print(sum(5))