"""
CP1404/CP5632 Practical
Hexadecimal colour code dictionary
"""

COLOUR_CODES = {"AbsoluteZero": "#0048ba", "AcidGreen": "#b0bf1a", "AliceBlue": "f0f8ff", "AlizarinCrimson": "#e32636",
                "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc", "Aqua": "#00ffff",
                "Aureolin": "#fdee00", "Beige": "#f5f5dc"}

for state_code in STATE_NAMES:
    print(f"{state_code:3} is {STATE_NAMES[state_code]}")

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", STATE_NAMES[state_code])
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
