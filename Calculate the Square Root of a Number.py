import math

num = float(input("Enter a number: "))
if num >= 0:
    sqrt = math.sqrt(num)
    print(f"The square root of {num} is {sqrt:.2f}")
else:
    print("Negative numbers do not have real square roots.")
