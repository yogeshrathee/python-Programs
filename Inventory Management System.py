inventory = {}

while True:
    print("Options:")
    print("1. Add Item")
    print("2. Update Item")
    print("3. Delete Item")
    print("4. View Inventory")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item_name = input("Enter item name: ")
        item_quantity = int(input("Enter item quantity: "))
        inventory[item_name] = item_quantity
        print("Item added.")
    elif choice == "2":
        item_name = input("Enter item name to update: ")
        if item_name in inventory:
            new_quantity = int(input("Enter new quantity: "))
            inventory[item_name] = new_quantity
            print("Item updated.")
        else:
            print("Item not found in inventory.")
    elif choice == "3":
        item_name = input("Enter item name to delete: ")
        if item_name in inventory:
            del inventory[item_name]
            print("Item deleted.")
        else:
            print("Item not found in inventory.")
    elif choice == "4":
        if not inventory:
            print("Inventory is empty.")
        else:
            print("Inventory:")
            for item, quantity in inventory.items():
                print(f"{item}: {quantity}")
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
