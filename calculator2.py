'''print("Select an operation to perform:")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid input. Please enter valid numeric values.")
    exit()

if operation == "1":
    result = num1 + num2
elif operation == "2":
    result = num1 - num2
elif operation == "3":
    result = num1 * num2
elif operation == "4":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero is not allowed.")
        exit()
else:
    print("Invalid operation. Please choose 1, 2, 3, or 4.")
    exit()

print(f"Result: {result:.2f}")'''