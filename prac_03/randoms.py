"""
CP1404/CP5632 - Practical
Experimenting with random module
"""

import random

"Line 1 test: print(random.randint(5, 20))"
line_one_result = 6, 8, 9, 15
"The smallest number I could have seen is 5 and largest is 20"

"Line 2 test: print(random.randrange(3, 10, 2))"
line_two_result = 5, 5, 9, 7
"The smallest number I could have seen is 3 and largest is 9. "
"This line could not have produced a 4."

"Line 3 test: print(random.uniform(2.5, 5.5))"
line_three_result = 3.3052967665449433, 4.779918534838799, 2.947026060459211
"smallest number 2.5000000000000001, largest number 5.5"

print(random.randint(1, 100))
