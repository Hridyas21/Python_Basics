todo_list=[]
while True:
    print("\n=====To-Do List======")
    print("1.Add Tasks\n2.Show Tasks\n3.Mark task as done\n4.Exit")
    
    ch=int(input("Enter your choice:"))
    
    if ch==1:
        task_num=int(input("How many task you want to add:"))
        for i in range(task_num):
            task=input(("Enter the task:"))
            todo_list.append(task)
            print("Task Added")
            
    elif ch==2:
        print("==Tasks==")
        for task_num,task in enumerate(todo_list,1):
            print(task_num,task)
        
    elif ch==3:
        done=int(input("Enter the task number to marked as done:"))
        print(f"Task {done} is marked as done")
        todo_list.pop(done-1)
        
    elif ch==4:
        break