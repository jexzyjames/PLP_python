def basic_calculator():
    """
    A simple Python program that performs basic arithmetic operations
    (addition, subtraction, multiplication, division) based on user input.
    """
    print("Welcome to the Basic Calculator!")

    try:
        # Get the first number from the user
        num1_str = input("Enter the first number: ")
        num1 = float(num1_str) # Convert input to a float to handle decimals

        # Get the second number from the user
        num2_str = input("Enter the second number: ")
        num2 = float(num2_str) # Convert input to a float

        # Get the operation from the user
        operation = input("Enter the operation (+, -, *, /): ")

        result = None # Initialize result variable

        # Perform the chosen operation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0: # Check for division by zero
                result = num1 / num2
            else:
                print("Error: Division by zero is not allowed.")
                return # Exit the function if division by zero occurs
        else:
            print("Error: Invalid operation. Please choose from +, -, *, or /.")
            return # Exit if the operation is invalid

        # Print the result in the desired format
        if result is not None:
            # Convert result to int if it's a whole number for cleaner output
            if result == int(result):
                result = int(result)
            print(f"{num1_str} {operation} {num2_str} = {result}")

    except ValueError:
        # Handle cases where the user inputs non-numeric values
        print("Error: Invalid number input. Please enter numerical values only.")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")

# Call the function to run the calculator
if __name__ == "__main__":
    basic_calculator()
