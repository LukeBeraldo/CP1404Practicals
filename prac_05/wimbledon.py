"""
Emails
Estimate: 30 minutes
Actual:   40 minutes
"""
CHAMPION_INDEX = 2

record_entry = []
with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
    in_file.readline()  # Is this the only way to get rid of the first row?
    for line in in_file:
        parts = line.strip().split(",")
        record_entry.append(parts)

    champion_to_wins = {}
    for record in record_entry:
        try:
            champion_to_wins[record[CHAMPION_INDEX]] += 1
        except KeyError:
            champion_to_wins[record[CHAMPION_INDEX]] = 1

    for name, count in champion_to_wins.items():
        print(f"{name} {count}")
