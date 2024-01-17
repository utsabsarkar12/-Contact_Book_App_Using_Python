Contact = {}

def display():
    print(Contact.items())
    print("Name \t Contact")
    for key in Contact:
        print("{} \t {}".format(key,Contact.get(key)))


while True:
    choise = int (input("1. Add New Contact \n"
                   "2. Search Contact \n"
                   "3. Display Contact \n"
                   "4. Edit Contact \n"
                   "5. Delete Contact \n"
                   "6. Exit \n"
                   "Please Write Number Between 1-6: "))


    if choise == 1:
        name = input("Add Your Contact Name: ")
        phone = input("Add Your Phone Number: ")

        Contact[name] = phone

        print("Contact Add Successfully")

    elif choise == 2:
        ContactName = input("Search Contact")
        if ContactName in Contact:
            print(ContactName,"Contact Number = " ,Contact[ContactName])

        else:
            print("Not Found")

    elif choise == 3:
        if not Contact:
            print("Contact Book Is Empty.")
        else:
            display()

    elif choise == 4:
        EditContact = input("Edit Your Contact: ")

        if EditContact in Contact:
            phone = input("Change Your Number: ")
            Contact[EditContact] = phone
            print("Contact Updated.")
            display()
        else:
            print("Name is not found")

    elif choise == 5:
        DeleteContact = input("Which Contact Do You Want To Delete?: ")

        if DeleteContact in Contact:
            DeleteConfirm = input("do you want to delete this contact y/n")

            if DeleteConfirm == "y" or DeleteConfirm == "Y":
                Contact.pop(DeleteContact)

            display()

        else:
            print("Name is not found.")

    else:
        break

