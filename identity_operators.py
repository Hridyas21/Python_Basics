#is 

a='abc' #a=10
b='abc' #b=10
print(a==b)
print(a is b) #is:returns True if both the variables are same objects.

ab=[12,'cat',12]
cd=[12,'cat',12]
print(ab==cd)
cd=ab
print(id(ab))
print(id(cd))
print(ab is cd)

ab=[12,'cat',12]
cd=[12,'cat',12]
ab=cd
print(ab is cd)

#is not
a=10
b=23
print(a is not b)

ab=[12,'cat',12]
cd=[12,'cat',12]
ab=cd
print(ab is not cd)