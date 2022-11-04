"""
Emails
Estimate: 30 minutes
Actual:   40 minutes
"""
CHAMPION_INDEX = 2
COUNTRIES_INDEX = 1


def main():
    """Get record data and display information about Wimbledon champions and there countires """
    record_entries = get_records()
    champion_to_wins, countries = process_information(record_entries)
    display_information(champion_to_wins, countries)


def get_records():
    """Get records from file and add to a list"""
    record_entries = []
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Is this the only way to get rid of the first row?
        for line in in_file:
            parts = line.strip().split(",")
            record_entries.append(parts)
    return record_entries


def process_information(record_entries):
    """Map champion and number of wins to a dictionary and add winning country to a set"""  # SRP?
    champion_to_wins = {}
    countries = set()
    for record in record_entries:
        countries.add(record[COUNTRIES_INDEX])
        try:
            champion_to_wins[record[CHAMPION_INDEX]] += 1
        except KeyError:
            champion_to_wins[record[CHAMPION_INDEX]] = 1
    return champion_to_wins, countries


def display_information(champion_to_wins, countries):
    print("Wimbledon Champions:")
    for name, count in champion_to_wins.items():
        print(f"{name} {count}")

    print(f"These {len(countries)} countries have won Wimbledon")
    # couldn't figure out list comprehension, got it from solutions
    print(", ".join(country for country in sorted(countries)))


main()
