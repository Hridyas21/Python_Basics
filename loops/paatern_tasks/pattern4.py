#Pattern - 4
'''
1
2 6
3 7 10
4 8 11 13
5 9 12 14 15
'''
cnt=4
for i in range(1,6):
    num=i
    for j in range(i):
        print(num,end=" ")
        num=num+(cnt-j)
    print(" ")