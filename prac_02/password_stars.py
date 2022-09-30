"""Password Printer with error checking"""

minimum_length = 8
password = input("Enter password: ")
while len(password) < minimum_length:
    print("Password too short")
    password = input("Enter password: ")
print(f"{'*' * len(password)}")
