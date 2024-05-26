number_1 = input('Enter your first number: ')
number_2 = input('Enter your second number: ')

try:
    num1 = float(number_1)
    num2 = float(number_2)
except ValueError:
    print("Invalid input. Please enter valid numeric values.")
    exit()

operation = input("Select an operation (+, -, *, /): ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero is not allowed.")
        exit()
else:
    print("Invalid operation. Please choose +, -, *, or /.")
    exit()

print(f"Result: {result}")
