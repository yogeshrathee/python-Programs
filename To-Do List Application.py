tasks = []

while True:
    print("Options:")
    print("Enter 'add' to add a task")
    print("Enter 'view' to view tasks")
    print("Enter 'quit' to quit the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input == "add":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added.")
    elif user_input == "view":
        print("Tasks:")
        for task in tasks:
            print(task)
    else:
        print("Invalid input")

