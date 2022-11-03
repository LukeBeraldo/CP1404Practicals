"""
CP1404/CP5632 Practical
Hexadecimal colour code dictionary
"""

COLOUR_TO_CODE = {"AbsoluteZero": "#0048ba", "AcidGreen": "#b0bf1a", "AliceBlue": "f0f8ff",
                  "AlizarinCrimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc",
                  "Aqua": "#00ffff", "Aureolin": "#fdee00", "Beige": "#f5f5dc"}

for colour_name in COLOUR_TO_CODE:
    print(f"{colour_name} is {COLOUR_TO_CODE[colour_name]}")

colour_name = input("\nEnter colour name: ").title()
while colour_name != " ":
    try:
        print(f"{colour_name} is, {COLOUR_TO_CODE[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").title()
