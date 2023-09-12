print('''
+ Addition
- subtraction
* Multiply
/ Divide
''')
num1 = int(input("Enter the first value (integer type):: "))
num2 = int(input("Enter the second value (integer type):: "))
opr = input("Enter the operator(+,-,*,/):: ")
if opr == "+":
    print(num1 + num2)
elif opr == "-":
    print(num1 - num2)
elif opr == "*":
    print(num1 * num2)
elif opr == "/":
    print(num1 / num2)
else:
    print("invalid operator !!!!")

