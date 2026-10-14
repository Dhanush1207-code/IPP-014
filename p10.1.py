stack = []

# Push operation


def push():
    item = int(input("Enter an element to push: "))
    stack.append(item)
    print("Element pushed successfully.")

# Pop operation


def pop():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("Popped element:", stack.pop())

# Display operation


def display():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("Stack elements:", stack)


# Menu-driven program
while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
    elif choice == 4:
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")
