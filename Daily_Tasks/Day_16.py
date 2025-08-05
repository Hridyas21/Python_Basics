#1. Generate squares of numbers from 1 to 10 using list comprehension
squares = [x * x for x in range(1, 11)]
print(squares)

#2. Extract all vowels from the string 'Python Programming is fun!
s="Python Programming is fun!"
v=["a","e","i","o","u"]
for char in s:
    if char in v:
        print(char)
        
#3. Filter out even numbers from a list of integers from 1 to 20
l=[]
for i in range(1,21):
    if i%2==0:
        l.append(i)
print(l)