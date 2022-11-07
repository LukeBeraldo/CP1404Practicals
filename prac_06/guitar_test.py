"""
CP1404/CP5632 Practical - guitar_test
Expected time: 20 mins
Actual time: 35 mins
"""

from guitar import Guitar


def main():
    """Pineapple"""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 10000.0)
    print(gibson.get_age())
    print(gibson.is_vintage())
    print(another_guitar.get_age())
    print(another_guitar.is_vintage())


main()
