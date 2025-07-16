num=int(input("Enter a number:"))
n=num
rev=0
while(num!=0):
    r=num%10
    rev=rev*10+r
    num=num//10
if(rev==n):
    print("Number is palindrome")
else:
    print("Number is not palindrome")
    