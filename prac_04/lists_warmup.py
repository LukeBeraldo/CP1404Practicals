"""
CP1404/CP5632 - Practical
Basic list exercises
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0] will give 3
# numbers[-1] will give 2
# numbers[3] will give 1
# numbers[:-1] will give 3, 1, 4, 1, 5, 9
# numbers[3:4] will give 1
# 5 in numbers will give True
# 7 in numbers will give False
# "3" in numbers will give False
# numbers + [6, 5, 3] will give [3, 1, 4, 5, 9, 2, 6, 5, 3]

numbers[0] = "ten"  # 1.
numbers[-1] = 1  # 2.
print(numbers[2:])  # 3.
print(9 in numbers)  # 4.
