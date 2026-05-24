from calculator import add, subtract, multiply, divide


def show_menu():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")


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

        if choice == "5":
            print("Goodbye! Mate, We meet again")
            break

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
