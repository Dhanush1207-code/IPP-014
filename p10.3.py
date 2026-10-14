def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    with open("contacts.txt", "a") as file:
        file.write(name + "," + phone + "," + email + "\n")

    print("Contact saved successfully!")


def display_contacts():
    try:
        with open("contacts.txt", "r") as file:
            print("\n--- Saved Contacts ---")
            contacts = file.readlines()

            if not contacts:
                print("No contacts found.")
            else:
                for contact in contacts:
                    name, phone, email = contact.strip().split(",", 2)
                    print("Name:", name)
                    print("Phone:", phone)
                    print("Email:", email)
                    print("--------------------")

    except FileNotFoundError:
        print("No contacts found. Please add a contact first.")


while True:
    print("\n1. Add Contact")
    print("2. Display Contacts")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        display_contacts()
    elif choice == "3":
        print("Exiting Contact Management System.")
        break
    else:
        print("Invalid choice. Please try again.")
