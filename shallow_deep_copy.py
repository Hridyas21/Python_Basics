my_list=[[23,12,5],["Hridya","Kichu","Devu"]]
g=my_list
g[0][1]="ABC"  #This does not create a copy, it just makes g another name for the same list in memory.
               #modifying the inner list of the same object.
print(g)
print(my_list) 

#shallow copy
#shallow changes the inner list, so original got affected.

import copy
my_list=[[23,12,5],["Hridya","Kichu","Devu"]]
g=copy.copy(my_list)
g[0][1]="ABC"  
print(g)
print(my_list)

#Deep copy -- original list will not be changed.
#Deep makes a complete copy including inside lists, so original didn’t change.

import copy
my_list=[[23,12,5],["Hridya","Kichu","Devu"]]
g=copy.deepcopy(my_list) 
g[0][1]="ABC"  
print(g)
print(my_list)
