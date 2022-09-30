"""
CP1404/CP5632 - Practical
Get a valid password using minimum length and display with asterisks
"""

MINIMUM_LENGTH = 8


def main():
    """Get a password and print it using functions"""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    """Get password and check it meets a minimum length"""
    password = input("Enter password: ")
    while len(password) < minimum_length:
        print("Password too short")
        password = input("Enter password: ")
    return password


def print_asterisks(string):
    """Print as many asterisks as there are in the string"""
    print(f"{'*' * len(string)}")


main()
