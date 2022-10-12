"""
CP1404/CP5632 - Practical
Fixed program to determine score status using functions
"""


def main():
    """Get a score and display its status """
    score = float(input("Enter score: "))
    print(determine_grade(score))


def determine_grade(score):
    """Determine the status of score pass in"""
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
