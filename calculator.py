def calculator():
    print("Welcome to Simple Calculator!")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    while True:
        # Get user input
        choice = input("\nEnter the number corresponding to the operation (1-5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please select a valid operation.")
            continue

        try:
            # Input numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Perform operations
            if choice == '1':
                result = num1 + num2
                print(f"The result of {num1} + {num2} is {result}")
            elif choice == '2':
                result = num1 - num2
                print(f"The result of {num1} - {num2} is {result}")
            elif choice == '3':
                result = num1 * num2
                print(f"The result of {num1} * {num2} is {result}")
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print(f"The result of {num1} / {num2} is {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

# Run the calculator
if __name__ == "__main__":
    calculator()
