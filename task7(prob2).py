ToDolist=[]

def add_task(task):
    ToDolist.append(task)
    #print(f"{task} added successfully!")

def view_tasks():
    for i in range(len(ToDolist)):
        print(f"tasks:{ToDolist[i]}")


def mark_task_completed(task):
    if task in ToDolist:
        index=ToDolist.index(task)
        ToDolist[index]=mark_task_completed
        #print(f"{task} marked as completed!")


def delete_task(task):
    if task in ToDolist:
        index=task.index(task)
        ToDolist.pop(index)
        #print(f"task:{task} deleted successfully! ")


def main():
    while True:
        print("1. Add task:")
        print("2. View tasks:")
        print("3. Complete tasks:")
        print("4. Delete task:")
        print("5. Exit")
        option=int(input("Enter an option:"))

        if option==1:
            task=input("Add task:")
            add_task(task)
            print(f"Task: {task} added successfully!")

        elif option==2:
            view_tasks()


        elif option==3:
            task=input("Enter task:")
            if task in ToDolist:
                mark_task_completed(task)
                print(f"Task: {task} completed!")
            else:
                print(f"Task: {task} not found!")


        elif option==4:
            task=input("Enter task:")
            if task in ToDolist:
                delete_task(task)
                print(f"Task: {task} deleted successfully!")
            else:
                print(f"Task:{task} not found!")
        
        
        
        elif option==5:
            break

        else:
            print("invalid option!")

main()










