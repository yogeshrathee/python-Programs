def calculate_hcf(x, y):
    if y == 0:
        return x
    else:
        return calculate_hcf(y, x % y)


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

hcf = calculate_hcf(num1, num2)
print(f"The HCF of {num1} and {num2} is {hcf}.")
