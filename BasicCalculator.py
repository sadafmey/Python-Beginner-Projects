def add(x, y):
    """Adds two numbers. Because sometimes, life just needs a little extra 'sum'thing!"""
    return x + y

def subtract(x, y):
    """Subtracts two numbers. Don't worry, we'll help you 'subtract' your problems away."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers. When in doubt, just 'multiply' your options!"""
    return x * y

def divide(x, y):
    """Divides two numbers. Handles division by zero with a touch of grace."""
    if y == 0:
        return "Error! Division by zero is like dividing by the number of unicorns in your backyard—undefined!"
    else:
        return x / y

def calculator():
    """Main function to perform arithmetic operations. Get ready to crunch some numbers!"""
    print("Welcome to My Basic Calculator!")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
            
            # Ask user if they want to continue
            another_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if another_calculation.lower() != 'yes':
                print("Thank you for using My Basic Calculator! May your calculations always add up!")
                break
        else:
            print("Invalid input. Please enter a valid option.")

if __name__ == "__main__":
    calculator()
