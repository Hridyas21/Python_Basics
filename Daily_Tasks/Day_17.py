#1. Extract the first and last character of a string: 
text = "Programming" 
print(text[0], text[-1]) 

#2. Reverse a string: 
reversed_text = text[::-1] 
print(reversed_text) 

#3. Count occurrences of a specific character: 
print(text.count("m")) 

#4. Replace spaces with underscores: 
sentence = "Python is fun to learn" 
print(sentence.replace(" ", "_")) 

#5. Check if a string is a palindrome: 
word = "madam" 
if word == word[::-1]:
    print("palindrome")
else:
    print("Not palindrome")