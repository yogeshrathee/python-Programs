decimal = int(input("Enter a decimal number: "))
binary = bin(decimal).replace("0b", "")
print(f"The binary representation of {decimal} is {binary}.")
