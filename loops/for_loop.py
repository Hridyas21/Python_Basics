#List
list1=[12,34,45,6,32]
# for ele in list1:
#     #print(ele)
#     print(ele,end=" ")
print(list(enumerate(list1,6))) #simply printing is done by type casting
    
for ind,ele in enumerate(list1): #returns with index, enumerate(list1,5) will start the indexing from 5
    print(ind,ele)
    
#string
name="hridya"
for char in name:
    print(char,end=" ")
    
#dictionary
dict1={"name":"hridya","age":21,"hobbies":["singing","dancing","coding"]}

for key in dict1:
    #print(key,end=" ") #key will be printed
    print(dict1[key],end=" ") #to print values in dictionary
    
print(" ")

for key in dict1.items(): #returns the key-value pairs in tuple
    print(key,end=" ") 

print(" ")

for key in dict1.keys(): #returns the keys
    print(key,end=" ")  

print(" ")

for val in dict1.values(): #returns the values
    print(val,end=" ") 

print(" ")

for key,val in dict1.items():
    print(key,val)

tuple
tuple1=("apple","banana","orange",23,23)
for ele in tuple1:
    print(ele,end=" ")
 
 
#The zip() function combines two lists element by element (i.e., position-wise).   
#It stops when the shortest list ends  
for k in zip(["name","age",23],["John",34,9]): 
    print(k)
    
for k,v in zip(["name","age",23],["John",34,9]): 
    print(v)