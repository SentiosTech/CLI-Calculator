# main.py

"""
This is a simple command-line calculator that performs basic arithmetic operations.
It supports square root, power, addition, subtraction, multiplication, and division.
"""

# Import the required arithmetic functions and input helper from the calculator module
from calculator.calculator import square_root, power, sume, subtract, multiply, division, get_float_input

def show_menu():
    """
    Displays the operation menu available to the user.
    """
    print(
        """\nOperation Menu: 
  1. Square Root
  2. Power
  3. Addition
  4. Subtraction
  5. Multiplication
  6. Division
  7. Exit Program
        """
    )

def handle_square_root():
    """
    Asks the user for a number, validates that it is not negative, and displays its square root.
    Repeats the process if an invalid number is provided.
    """
    print("\nYou selected the square root operation.")
    print("Please enter a number to calculate its square root.")

    while True:
        num = get_float_input("Type a number to calculate its square root: ")
        if num < 0:
            print("Cannot calculate square root of a negative number.")
        else:
            result = square_root(num)
            print(f"The result of square root operation is: {result:.3f}\n")
            break

def handle_two_numbers_operation(operation_name, operation_func):
    """
    Handles operations that require two numbers, such as power, addition, subtraction, multiplication, and division.
    Receives the operation name (for display purposes) and the corresponding function.

    If the operation is division, it validates that the second number is not zero.
    """
    print(f"\nYou selected the {operation_name} operation.")
    print("Please enter two numbers.")

    num1 = get_float_input("Type first number: ")
    num2 = get_float_input("Type second number: ")

    if operation_name == "division":
        while num2 == 0:
            print("Cannot divide by zero.")
            num2 = get_float_input("Please enter a non-zero second number: ")

    result = operation_func(num1, num2)
    print(f"The result of {operation_name} operation is: {result:.3f}\n")

def run_calculator():
    """
    Program's main function.
    Displays the menu, receives and validates user input, and calls the appropriate function
    to perform the selected operation.
    """
    print("Welcome, this is a simple calculator")

    while True:
        show_menu()
        
        # Prompt the user to choose an operation
        try:
            option = int(input("Choose an option from 1 - 7: "))
            if option < 1 or option > 7:
                print("Invalid option. Please choose a number between 1 and 7.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")
            continue

        # Mapping menu options to corresponding functions
        if option == 1:
            handle_square_root()
        elif option == 2:
            handle_two_numbers_operation("power", power)
        elif option == 3:
            handle_two_numbers_operation("addition", sume)
        elif option == 4:
            handle_two_numbers_operation("subtraction", subtract)
        elif option == 5:
            handle_two_numbers_operation("multiplication", multiply)
        elif option == 6:
            handle_two_numbers_operation("division", division)
        elif option == 7:
            print("Exiting...")
            break

# Program entry point: only runs the function run_calculator() if this file is executed directly
if __name__ == "__main__":
    run_calculator()
