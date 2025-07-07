#int
a=3
print(type(a))

#float
a=2.2
print(type(a))

#complex
a=3j #In python, j is used for imaginary part instead of i
print(type(a))
#
#string
a="python"
print(type(a))

#list
list1=['python',23,34.4,['hridya',34]]
print(type(list1))

print(list1[2])

print(list1[3][0]) #to get the element of list inside the list1
print(list1[-1][1]) #By reverse indexing
#print(a[1])

#to change
list1[0]='cat'
print(list1)

#tuple
s=('python',23,34.4,['hridya',34])
print(s[1])
#s[1]='hridya' --->this will not support in tuple, since tuple is immutable


#set
b={12,'hridya',12,23.1}
print(b)

print(type("string")); print(type(23))--->The type will be string and int not tuple, until separated  by commas

s='hridya'
print(s[1])
s[1]='w' #This will gives a typeerror , since strings cannot be changed
print(s)

#Dictionary
#Data is stored as key:value pairs
#values are accessed by key
#values can be changed

dict1={"name":"Kichu","age":21,20:12,"hobbies":["singing","dancing","coding"]} #list can be given as values, but not key
print(dict1["name"])
print(dict1["hobbies"]) #values will be printed
print(dict1["hobbies"][1])
dict1["name"]="Devu" #Values can be changed
print(dict1)

#Boolean
True
False

a,b,c=['python',23,54]
print(b)#---->This will gives 23 as output, ie list can be unpacked