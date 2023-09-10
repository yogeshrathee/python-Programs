n = int(input("Enter the number of elements: "))
numbers = [float(input(f"Enter number {i + 1}: ")) for i in range(n)]
sum_of_numbers = sum(numbers)
average = sum_of_numbers / n
print(f"Sum of numbers: {sum_of_numbers}")
print(f"Average of numbers: {average}")
