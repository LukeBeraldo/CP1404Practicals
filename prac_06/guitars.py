"""
CP1404/CP5632 Practical - guitar_test
Expected time: 45 mins
Actual time:  1 hour
"""

from guitar import Guitar


def main():
    """Guitar program, using guitar class"""
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = input("Year: ")
        cost = input("Cost: $")
        guitar = Guitar(name, year, cost)
        print(f"{guitar} added.")
        guitars.append(guitar)
        name = input("Name: ")

    print("These are my guitars:\n")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(Vintage)"
        print(f"Guitar {i}: {guitar.name:>20}, ({guitar.year}), worth $ {guitar.cost:10,.f}{vintage_string}")


main()
