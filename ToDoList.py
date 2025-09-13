# Simple To-Do List in Python (Console Version)

# A list to store all tasks
todo_list = []

# Function to display the menu
def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

# Main program loop (runs until the user chooses Exit)
while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")  # Get user input

    # Option 1: Show all tasks
    if choice == "1":
        if not todo_list:  # If list is empty
            print("\nNo tasks in the list!")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")  # Display tasks with numbers

    # Option 2: Add a new task
    elif choice == "2":
        task = input("Enter a new task: ")
        todo_list.append(task)  # Add task to list
        print(f"Task '{task}' added!")

    # Option 3: Remove an existing task
    elif choice == "3":
        if not todo_list:  # If list is empty
            print("No tasks to remove!")
        else:
            # Show all tasks with numbers
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter task number to remove: "))
                removed = todo_list.pop(task_num - 1)  # Remove task by index
                print(f"Task '{removed}' removed!")
            except (ValueError, IndexError):
                print("Invalid task number!")  # Handle wrong input

    # Option 4: Exit the program
    elif choice == "4":
        print("Goodbye!")
        break  # Exit the loop

    # If input is not 1-4
    else:
        print("Invalid choice! Try again.")
