class PersonalFinanceManager:
    def __init__(self):
        self.income = 0
        self.expenses = []

    def add_income(self, amount):
        self.income += amount

    def add_expense(self, description, amount):
        self.expenses.append((description, amount))

    def view_summary(self):
        total_expenses = sum(amount for _, amount in self.expenses)
        balance = self.income - total_expenses
        print(f"Income: ${self.income}")
        print(f"Total Expenses: ${total_expenses}")
        print(f"Balance: ${balance}")


finance_manager = PersonalFinanceManager()

while True:
    print("Options:")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Summary")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter income amount: "))
        finance_manager.add_income(amount)
        print("Income added.")
    elif choice == "2":
        description = input("Enter expense description: ")
        amount = float(input("Enter expense amount: "))
        finance_manager.add_expense(description, amount)
        print("Expense added.")
    elif choice == "3":
        finance_manager.view_summary()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
