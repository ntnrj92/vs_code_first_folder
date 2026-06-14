from calculator import add, subtract, multiply, divide, sqrt, cbrt


def show_menu():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square root")
    print("6. Cube root")
    print("7. Exit")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "7":
            print("Goodbye! I am on GitHub")
            break

        if choice in ("5", "6"):
            a = get_number("Enter the number: ")
            if choice == "5":
                result = sqrt(a)
                if result is None:
                    print("Cannot take square root of a negative number.")
                else:
                    print(f"Result: {result}")
            else:
                result = cbrt(a)
                print(f"Result: {result}")
        else:
            a = get_number("Enter the first number: ")
            b = get_number("Enter the second number: ")

        if choice == "1":
            result = add(a, b)
            print(f"Result: {result}")
        elif choice == "2":
            result = subtract(a, b)
            print(f"Result: {result}")
        elif choice == "3":
            result = multiply(a, b)
            print(f"Result: {result}")
        elif choice == "4":
            result = divide(a, b)
            if result is None:
                print("Cannot divide by zero.")
            else:
                print(f"Result: {result}")
        else:
            print("Please choose a valid option.")

        print()


if __name__ == "__main__":
    main()
