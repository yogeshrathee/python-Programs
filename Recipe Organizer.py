recipes = {}

while True:
    print("Options:")
    print("1. Add Recipe")
    print("2. View Recipes")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        recipe_name = input("Enter recipe name: ")
        ingredients = input("Enter ingredients (comma-separated): ").split(",")
        recipes[recipe_name] = ingredients
        print("Recipe added.")
    elif choice == "2":
        if not recipes:
            print("No recipes recorded yet.")
        else:
            print("Recipes:")
            for recipe, ingredients in recipes.items():
                print(f"{recipe}: {', '.join(ingredients)}")
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")

