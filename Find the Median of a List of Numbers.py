numbers = [float(input("Enter a number: ")) for _ in range(5)]
numbers.sort()
n = len(numbers)

if n % 2 == 0:
    median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
else:
    median = numbers[n // 2]

print(f"The median of the numbers is {median}.")
