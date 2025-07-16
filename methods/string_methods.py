language="pythoN"
language.upper()
print(language) #This will return the same 'python'; ie, it will not change the original string.

print(language.upper()) #this will return 'PYTHON'

print(language.lower())

print(language.capitalize())   #To capitalize the only first letter.

print(language.swapcase()) # To convert upper to lower and lower to upper

print(language[1])
print(language.startswith('p'))
print(language.endswith('N'))

print(language.count('p'))

#strip
sentence="  python is a high interpreted praogramming language  "
print(sentence)

print(sentence.strip()) #Strip will remove the whitespaces at the ends

#split
print(sentence.split()) #['python', 'is', 'a', 'high', 'interpreted', 'praogramming', 'language']
print(sentence.split('high')) #'high' will be removed and splits,['  python is a ', ' interpreted praogramming language  ']
print(sentence.partition('high'))#('  python is a ', 'high', ' interpreted praogramming language  ')
print(len(sentence))

