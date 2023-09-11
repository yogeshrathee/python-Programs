expenses = []

while True:
    print("Options:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        description = input("Enter expense description: ")
        amount = float(input("Enter expense amount: "))
        expenses.append((description, amount))
        print("Expense added.")
    elif choice == "2":
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print("Expenses:")
            for desc, amt in expenses:
                print(f"{desc}: ${amt}")
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")
