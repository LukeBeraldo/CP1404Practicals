"""
CP1404/CP5632 - Practical
Score Menu Exercise
"""

MENU_STRING = "(E)nter Score\n(R)esult\n(S)tars!\n(Q)uit"


def main():
    """Display Menu with options to enter a score, determine a result or print stars"""
    score = 0
    print(MENU_STRING)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "E":
            score = get_valid_score()
        elif choice == "R":
            print(f"Your score is {determine_status(score)}")
        elif choice == "S":
            print_asterisks(score)
        else:
            print("Invalid input")
        print(MENU_STRING)
        choice = input(">>> ").upper()
    print("Bye")


def get_valid_score():
    """Get a valid score between 0 and 100"""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def determine_status(score):
    """Determine the status of the score passed in"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_asterisks(score):
    """Print as many asterisks as the score"""
    print(f"{'*' * score}")


main()
