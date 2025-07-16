num=int(input("Enter a number:"))
n=num
sum=0
numstr=str(n)
l=len(numstr)
while(num!=0):
    r=num%10
    sum=sum+(r**l)
    num=num//10
if(sum==n):
    print("Number is armstrong")
else:
    print("Number is not armstrong")