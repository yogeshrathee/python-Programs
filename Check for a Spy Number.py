def is_spy_number(num):
    num_str = str(num)
    sum_of_digits = sum(int(digit) for digit in num_str)
    product_of_digits = 1
    for digit in num_str:
        product_of_digits *= int(digit)
    return sum_of_digits == product_of_digits


num = int(input("Enter a number: "))

if is_spy_number(num):
    print(f"{num} is a spy number.")
else:
    print(f"{num} is not a spy number.")
