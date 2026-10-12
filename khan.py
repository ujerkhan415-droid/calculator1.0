# Calculator 1.0
# Simple Python calculator with basic arithmetic operations

print("Calculator 1.0")
print("Operations: +, -, *, /")

while True:
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = num1 / num2
        else:
            print("Invalid operator. Please use +, -, *, /")
            continue

        print(f"Result: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values only.")

    choice = input("Do you want to calculate again? (y/n): ").lower()
    if choice != 'y':
        print("Thanks for using Calculator 1.0")
        break
