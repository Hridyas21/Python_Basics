todo_list=[]

def AddTask():
    task_id=int(input("How many task you want to add :"))
    for i in range(task_id):
        task=input("Enter the task:")
        todo_list.append([task,False])
        print("Task added successfully.") 
    
      

def UpdateTask():
    try:
        task_id=int(input("Enter task id to update:"))
        todo_list[task_id-1][1]=not todo_list[task_id-1][1]
        stat="completed" if todo_list[task_id-1][1] else "Not completed"
        print(f"Task {task_id} is updated as {stat}")
    except Exception as e:
        print(e)
        print("Failed to update task")
                
    
def RemoveTask():
    try:
        task_id=int(input("Enter task id to be removed:"))
        todo_list.pop(task_id-1)
        print(f"Task {task_id} has removed.")
    except Exception as e:
        print(e)
        print("Failed to remove task")
        
        
def ShowTask():
    print("\n==Tasks==")
    if not todo_list:
        print("No tasks")
    else:
        #print("\n=====Tasks=====")
        for task_id,(task,status) in enumerate(todo_list,1):       
            print(f"{task_id}. {task} - {'Completed' if status else 'Not completed'}")


while True:
    print("\n=====To-Do List======")
    print("1.Add Tasks\n2.Show Tasks\n3.Update task\n4.Remove Tasks\n5.Exit\n")
    
    
    ch=int(input("Enter your choice:"))
    
        
    match ch:
        case 1:
            AddTask()
        case 2:
            ShowTask()
        case 3:
            UpdateTask()
        case 4:
            RemoveTask()
        case 5:
            print("Program Exited..!!")
            break
        case _:
            print("Invalid choice. Please enter a choice between 1-5")