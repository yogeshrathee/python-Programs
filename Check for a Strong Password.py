import re

password = input("Enter a password: ")

if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password):
    print("Strong password!")
else:
    print("Weak password. Please follow password guidelines.")
