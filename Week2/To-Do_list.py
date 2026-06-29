#To-do list
To_Do_list=["read","write","Take notes"]

def add_task():
        task=input("Add a task: ")
        To_Do_list.append(task)
        print("Task added")

def remove_task():
        task=input("Enter the task that you want to remove: ")
        try:
            task in To_Do_list
            To_Do_list.remove(task)
        except ValueError :
            print("Task is not in list")

def show_tasks():
    print("-----To-Do list-----")
    for task in To_Do_list:
        print(task)

while True:
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Show Tasks")
    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_task()
        elif choice == 2:
            remove_task()
        elif choice == 3:
            show_tasks()
            break
    except ValueError:
        print("Invalid choice")