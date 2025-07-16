#Pattern - 3
'''
A
A B
A B C
A B C D
A B C D E

Hint
print(chr(65))  --> A
chr(65)  represents A and chr(66) represents B '''

for i in range(1,6):
    for j in range(0,i):
        print(chr(65+j),end=" ")
        
    print(" ")