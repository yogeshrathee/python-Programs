n = int(input("Enter a positive integer: "))
sum_of_squares = sum([i ** 2 for i in range(1, n + 1)])
print(f"The sum of squares of {n} natural numbers is {sum_of_squares}.")
