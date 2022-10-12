"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):  # Its creating AND printing the report so problem with SRP?
    """Print income report"""
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes, 1):
        total += income
        print(f"Month {month} - Income: ${income} Total: ${total}")


main()

# check answers
