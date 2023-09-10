def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input("Enter a number: "))
temp = num
sum_of_factorial_digits = sum([factorial(int(digit)) for digit in str(num)])

if sum_of_factorial_digits == num:
    print(f"{num} is a strong number.")
else:
    print(f"{num} is not a strong number.")
