"""
Emails
Estimate: 30 minutes
Actual:   40 minutes
"""
CHAMPION_INDEX = 2
COUNTRIES_INDEX = 1


def main():
    """Get record data and display information about Wimbledon champions and there countires """
    get_records()


def get_records():
    """Get records from file and add to a list"""
    record_entry = []
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Is this the only way to get rid of the first row?
        for line in in_file:
            parts = line.strip().split(",")
            record_entry.append(parts)
    return record_entry

    champion_to_wins = {}
    countries = set()
    for record in record_entry:
        countries.add(record[COUNTRIES_INDEX])
        try:
            champion_to_wins[record[CHAMPION_INDEX]] += 1
        except KeyError:
            champion_to_wins[record[CHAMPION_INDEX]] = 1

    print("Wimbledon Champions:")
    for name, count in champion_to_wins.items():
        print(f"{name} {count}")

    print(f"These {len(countries)} countries have won Wimbledon")
    # couldn't figure out list comprehension, got it from solutions
    print(", ".join(country for country in sorted(countries)))
