#for loops using range
for i in range(8): 
    print(i)

for i in range(2,8):
    print(i)

for i in range(10):
    print("python")

for i in range(0,10,1) #for i in range(start,stop,step)
    print(i)

#multiplication table for a number
num=int(input("Enter the number:"))
for i in range(1,11):
    print(f"{i} * {num} = {i*num}")

#printing even numbers  
for num in range(1,17):
    if(num%2==0):
        print(num)
    

#From the given list of fruits print the fruits that starts with 'a'
fruits=["banana","apple","Avocado","orange"]
for fruit in fruits:
   
    if(fruit.capitalize().startswith("A")):
        print(fruit)

#Print  the words starts with vowels       
words=["Ant","boy","cat","umbrella","egg","ink","out"]
for word in words:
    if word[0].lower() in ["a","e","i","o","u"]: 
        print(word)

#print the frequency of the letters of the given string
str1="java"
d={}
for char in str1:
    """cnt=str1.count(char) #using in built method
    d.update({char:cnt})"""
    if char in d:
        d[char]+=1
    else:
        d[char]=1
print(d)
    #print(char,":",cnt)


#factorial of a number
num=int(input("Enter a number:"))
fact=1
if num==0 or num==1:
    print(1)
else:
    for i in range(1,num+1):
        fact=fact*i
print(fact)


    
for r in range(1,4):
    for j in range(1,r+1):
        print(j,end=" ")
    print("")

            