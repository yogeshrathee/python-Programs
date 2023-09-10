string = input("Enter a string: ")
vowels = "AEIOUaeiou"
count = 0

for char in string:
    if char in vowels:
        count += 1

print(f"The number of vowels in the string is {count}.")
