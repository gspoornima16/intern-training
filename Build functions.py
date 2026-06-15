#Contacts
Contact_book={"Anne":567234,"Baron":784567,"Claude":235698,"Den":547692}
def add_contact():
    Name=input("Enter the name: ")
    Phone=int(input("Enter the number: "))
    Contact_book[Name]=Phone
    print("Contact added")
def find_contact():
    Name=input("Enter the name: ")
    if Name in Contact_book:
        print(Name,Contact_book[Name])
    else:
        print("Contact is not found")
def list_contacts():
        print("----List of contacts----")
        for name, phone in Contact_book.items():
            print(name, ":", phone)
while True:
    print("1. Add contact")
    print("2. Find contact")
    print("3. list of contacts")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        find_contact()
    elif choice == "3":
        list_contacts()
        break
    else:
        print("Invalid choice")


#To-do list
To_Do_list=["read","write","Take notes"]

def add_task():
        task=input("Add a task: ")
        To_Do_list.append(task)
        print("Task added")

def remove_task():
        task=input("Enter the task that you want to remove: ")
        if task in To_Do_list:
            To_Do_list.remove(task)
        else:
            print("Task is not in list")

def show_tasks():
    print("-----To-Do list-----")
    for task in To_Do_list:
        print(task)

while True:
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Show Tasks")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        show_tasks()
        break
    else:
        print("Invalid choice")


