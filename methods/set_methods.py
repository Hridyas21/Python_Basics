set1={"apple",23,"banana",43}

set1.add("orange") #add new element

set1.update(["plum","grapes"]) #add elements from list 
set1.update(("name","Hridya")) #add elements from tuple

set1.remove("apple") #removes the given element. raises error if not present
set1.discard("apple") #removes the the given element. does not raise error
set1.pop() #Removes and returns a random element

print(set1)