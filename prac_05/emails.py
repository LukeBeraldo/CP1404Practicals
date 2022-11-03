"""
Emails
Estimate: 30 minutes
Actual:   40 minutes
"""


def main():
    email_to_name = {}
    user_email = input("Email: ")
    while user_email != "":
        name = extract_email_name(user_email)
        is_name = input(f"Is your name {name}? (Y/n): ")
        if is_name.upper() != "Y" and is_name != "":
            name = input("Name: ")
        email_to_name[user_email] = name
        user_email = input("Email: ")

    for user_email, name in email_to_name.items():
        print(f"{name} ({user_email})")


def extract_email_name(user_email):
    email_parts = user_email.split("@")
    return email_parts[0].title()


main()
