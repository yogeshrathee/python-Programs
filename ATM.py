
account_balance = 1000

\
def display_balance():
    print(f"Your account balance is ${account_balance:.2f}")


def deposit():
    global account_balance
    amount = float(input("Enter the amount to deposit: $"))
    account_balance += amount
    print(f"${amount:.2f} has been deposited into your account.")
    display_balance()


def withdraw():
    global account_balance
    amount = float(input("Enter the amount to withdraw: $"))
    if amount > account_balance:
        print("Insufficient funds.")
    else:
        account_balance -= amount
        print(f"${amount:.2f} has been withdrawn from your account.")
        display_balance()


while True:
    print("\nOptions:")
    print("1. Display Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Quit")

    choice = input("Select an option (1/2/3/4): ")

    if choice == '1':
        display_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        print("Thank you for using our ATM. Goodbye!")
        break
    else:
        print("Invalid option. Please choose a valid option.")
