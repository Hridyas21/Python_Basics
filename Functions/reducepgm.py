from functools import reduce #Import reduce because it is not a built-in function in Python — it's part of the functools module.
s=reduce(lambda a,b:a*b,range(1,6))
print(s)