principal = float(input("Enter the initial principal amount: "))
rate = float(input("Enter the annual interest rate (in percentage): "))
time = int(input("Enter the time period (in years): "))
monthly_deposit = float(input("Enter the monthly deposit amount: "))
compounds_per_year = int(input("Enter the number of times interest is compounded per year: "))

amount = principal
for month in range(12 * time):
    amount += monthly_deposit
    amount *= (1 + rate / (compounds_per_year * 100))

interest_earned = amount - (principal + (monthly_deposit * 12 * time))
print(f"The total amount after {time} years is {amount:.2f}")
print(f"The total interest earned is {interest_earned:.2f}")
