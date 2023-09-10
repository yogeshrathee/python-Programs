n = int(input("Enter the number of terms: "))
a, b = 0, 1
fib_sequence = []

while len(fib_sequence) < n:
    fib_sequence.append(a)
    a, b = b, a + b

print("Fibonacci Sequence:")
for term in fib_sequence:
    print(term, end=" ")
