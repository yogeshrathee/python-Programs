n = int(input("Enter the number of terms: "))
a, b = 0, 1
count = 0
while count < n:
    print(a, end=" ")
    temp = a
    a = b
    b = temp + b
    count += 1
