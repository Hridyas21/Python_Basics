dict1={"name":"hridya","age":21,"hobbies":["singing","dancing","coding"]}
print(dict1.items())#returns the key-value pairs in tuple

dict1.update({"name":"angel"})
dict1.update({'place':"Thrissur"})

dict1.pop('age') #removes the pair of given key
#dict1.popitem() #removes the last item, without giving index

print(dict1.get("name")) 
print(dict1.get("address","NOT PRESENT")) #if not present, NONE will be outpu, or we can give what to print

print(dict1["name"])#returns the value of the given key
dict1["4"]="laptop" #the new value "laptop will be added for the given key"
dict1["name"]="laptop" #the value of the given key will be updated with the given new value

dict1.setdefault("lsnguage","python") #adds the elements as key-value pair
print(dict1)



