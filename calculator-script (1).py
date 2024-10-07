def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def calculator():
    print("Simple Calculator")
    
    while True:
        try:
            # Enter numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            # Choose operation
            print("\nChoose operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exit")
            
            choice = input("Enter choice (1/2/3/4/5): ")
            
            # Perform calculation based on choice
            if choice == '1':
                result = add_numbers(num1, num2)
                operation = "Addition"
            elif choice == '2':
                result = subtract_numbers(num1, num2)
                operation = "Subtraction"
            elif choice == '3':
                result = multiply_numbers(num1, num2)
                operation = "Multiplication"
            elif choice == '4':
                result = divide_numbers(num1, num2)
                operation = "Division"
            elif choice == '5':
                print("Thank you for using the calculator. Goodbye!")
                break
            else:
                print("Invalid input. Please try again.")
                continue
            
            # Display result
            print(f"\n{operation} result: {result}")
            print()
            
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    calculator()
