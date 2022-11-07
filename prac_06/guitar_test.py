"""
CP1404/CP5632 Practical - guitar_test
Expected time: 1 hour
Actual time: 45 mins
"""

from guitar import Guitar


def main():
    """Pineapple"""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(gibson.get_age())
    print(gibson.is_vintage())


main()
