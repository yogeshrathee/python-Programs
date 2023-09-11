def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)


weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)

print("Your BMI is:", bmi)

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.9:
    print("Normal weight")
elif 24.9 <= bmi < 29.9:
    print("Overweight")
else:
    print("Obese")
