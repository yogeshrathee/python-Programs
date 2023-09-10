import random

min_value = int(input("Enter the minimum value: "))
max_value = int(input("Enter the maximum value: "))
random_number = random.randint(min_value, max_value)
print(f"Random number between {min_value} and {max_value}: {random_number}")
