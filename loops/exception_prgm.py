while True:
    try:
        a,b=map(int,input("Enter a number:").split())
        c=a/b
        print(c)
        break
    except Exception as e:
        print("Error:",e)
        print("Enter a valid number..!!")

