#Contacts
Contact_book={"Anne":567234,"Baron":784567,"Claude":235698,"Den":547692}
def add_contact():
    try:
        Name=input("Enter the name: ")
        Phone=int(input("Enter the number: "))
        Contact_book[Name]=Phone
        print("Contact added")
    except ValueError:
        print("Invalid input.enter numbers")
def find_contact():
    Name=input("Enter the name: ")
    try:
        Name in Contact_book
        print(Name,Contact_book[Name])
    except KeyError:
        print("Contact is not found")
def list_contacts():
        print("----List of contacts----")
        for name, phone in Contact_book.items():
            print(name, ":", phone)
while True:
    print("1. Add contact")
    print("2. Find contact")
    print("3. list of contacts")
    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_contact()
        elif choice == 2:
            find_contact()
        elif choice == 3:
            list_contacts()
            break
    except ValueError:
        print("Invalid choice")