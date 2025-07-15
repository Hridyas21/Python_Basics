n=int(input("Enter a number:"))
# pattern-1
for i in range(1,5):
    print("* "*i)
    
    
#pattern-2
'''1
   2,4
   3,6,9
   4,8,12,16'''

for i in range(1,5):
    for j in range(1,i+1):
        print(j*i,end=" ")
    print("")
        
        
for i in range(1,5):
    num=i
    for j in range(i):
        print(num,end=" ")
        num=num+i
    print("")
 
 #pattern-3   
for r in range(1,6):
    for sp in range(5-r):
        print(" ",end=(""))
    for st in range(r):
        print("*",end="")
    print("")

        #Another method by minimizing the loops
        
for r in range(1,6):
    print(" "*int(5-r),"*"*r)

for i in range(6,0,-1):
    print("*"*i)

for r in range(6,0,-1):
     print("* "*r," "*int(6-r))


