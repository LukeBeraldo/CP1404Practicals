"""
CP1404/CP5632 Practical
list_exercises using different functions
"""

NUMBER_OF_REPETITIONS = 5

numbers = []

for i in range(NUMBER_OF_REPETITIONS):
    number = int(input("Number: "))
    numbers.append(number)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

# check answers
