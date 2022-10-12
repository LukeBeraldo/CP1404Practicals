"""
CP1404/CP5632 Practical
list_exercises using different functions
"""

import random

NUMBERS_PER_PICK = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """ Quick Pick random numbers"""
    number_of_quick_picks = int(input("How many quick picks? "))

    for number in range(number_of_quick_picks):
        quick_pick = []
        for i in range(NUMBERS_PER_PICK):
            number = (random.randint(MINIMUM, MAXIMUM))
            while number in quick_pick:
                number = (random.randint(MINIMUM, MAXIMUM))
            quick_pick.append(number)
        quick_pick.sort()
        # "This is what I came up with but it gives you the generator object. Refresh/re-explain why it does this"
        # print(f"{number:2}" for number in quick_pick)
        "Corrected after looking at solutions"
        print(" ".join(f"{number:2}" for number in quick_pick))