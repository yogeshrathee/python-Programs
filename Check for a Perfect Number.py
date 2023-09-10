num = int(input("Enter a number: "))
sum_of_divisors = sum([i for i in range(1, num) if num % i == 0])

if sum_of_divisors == num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
