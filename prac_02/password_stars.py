"""Password Printer with error checking"""

MINIMUM_LENGTH = 8


def main():
    """Get a valid password"""
    password = get_password()
    print_password(password)


def print_password(password):
    print(f"{'*' * len(password)}")


def get_password():
    password = input("Enter password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Password too short")
        password = input("Enter password: ")
    return password


main()
