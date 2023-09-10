import math

num = int(input("Enter a number: "))

if 0 < num == math.isqrt(num) ** 2:
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")
