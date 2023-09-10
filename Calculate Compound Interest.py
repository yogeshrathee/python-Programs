principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in percentage): "))
time = float(input("Enter the time period (in years): "))
compounds_per_year = float(input("Enter the number of times interest is compounded per year: "))

amount = principal * (1 + (rate / (compounds_per_year * 100))) ** (compounds_per_year * time)
interest = amount - principal

print(f"The compound interest is {interest:.2f}")
