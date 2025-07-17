list1=['python',23,'hridya',54]

print(list1.index('hridya'))
print(list1.count('python'))


list1.append('suresh') #Adds an item to the end of the list
list1.extend(['kichu','devu']) #Adds multiple elements from another list.

list1.remove(54) #Removes the value given from the list
list1.pop(1) #Removes element at the given index
list1.pop() #Removes the last element ,pop also returns the removed element

list1.insert(6,'devu') #Insert the given element at the given index

list1.sort() #sorts the original list in ascending order
list1.sort(reverse=True) # Sorts in descending order

list1.reverse() #Reverse the elements in the list

#slicing
print(list1[2:4]) #4th will not be included
print(list1) 

list1=[12,34,45,6,32]
print(list1[-1:2:-1]) #start,stop,step
