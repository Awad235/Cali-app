# calculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

def get_input():
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        return x, y
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return None, None

def display_menu():
    print("\n==== Calculator Menu ====")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("Choose an operation (1-5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please select a valid option.")
            continue

        x, y = get_input()
        if x is None or y is None:
            continue

        if choice == '1':
            print(f"Result: {x} + {y} = {add(x, y)}")
        elif choice == '2':
            print(f"Result: {x} - {y} = {subtract(x, y)}")
        elif choice == '3':
            print(f"Result: {x} * {y} = {multiply(x, y)}")
        elif choice == '4':
            result = divide(x, y)
            print(f"Result: {x} / {y} = {result}")

if __name__ == "__main__":
    main()

