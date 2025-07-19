def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

print("=== Simple Calculator ===")

while True:
    print("\nSelect operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter operation choice: ").strip()

    if choice == '5':
        print("Exiting Bye!")
        break

    if choice not in ('1', '2', '3', '4'):
        print("Please select a valid operation.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input!")
        continue

    if choice == '1':
        result = add(num1, num2)
        print(f"Result: {num1} + {num2} = {result}")

    elif choice == '2':
        result = subtract(num1, num2)
        print(f"Result: {num1} - {num2} = {result}")

    elif choice == '3':
        result = multiply(num1, num2)
        print(f"Result: {num1} * {num2} = {result}")
        
    elif choice == '4':
        result = divide(num1, num2)
        print(f"Result: {num1} / {num2} = {result}")