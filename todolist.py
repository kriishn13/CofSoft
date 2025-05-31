todo_list = []

def show_menu():
    print("\n---- To-Do List ----")
    print("1. Add")
    print("2. View")
    print("3. Remove")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        todo_list.append(task)
        print("Added.")

    elif choice == "2":
        print("\nYour Tasks:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

    elif choice == "3":
        task_no = int(input("Enter task number to remove: "))
        if 0 < task_no <= len(todo_list):
            removed = todo_list.pop(task_no - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")

    elif choice == "4":
        print("Exiting.")
        break

    else:
        print("Invalid choice. Try again.")
