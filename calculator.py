# Simple Calculator in Python (Console Version)

# Define functions for each operation
def add(x, y):
    return x + y  # Addition

def subtract(x, y):
    return x - y  # Subtraction

def multiply(x, y):
    return x * y  # Multiplication

def divide(x, y):
    if y == 0:  # Prevent division by zero
        return "Error! Division by zero."
    return x / y  # Division

# Main program loop (runs until user chooses to exit)
while True:
    # Display the menu
    print("\n===== CALCULATOR =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    # Get user choice
    choice = input("Enter choice (1-5): ")

    # Exit the program
    if choice == "5":
        print("Goodbye!")
        break  # Stop the loop

    # Check if user entered a valid operation
    if choice in ["1", "2", "3", "4"]:
        try:
            # Get numbers from user
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            # Handle invalid input (like letters instead of numbers)
            print("Invalid input! Please enter numbers only.")
            continue

        # Perform the selected operation
        if choice == "1":
            print(f"Result: {add(num1, num2)}")
        elif choice == "2":
            print(f"Result: {subtract(num1, num2)}")
        elif choice == "3":
            print(f"Result: {multiply(num1, num2)}")
        elif choice == "4":
            print(f"Result: {divide(num1, num2)}")
    else:
        # If user entered something not in 1–5
        print("Invalid choice! Try again.")
