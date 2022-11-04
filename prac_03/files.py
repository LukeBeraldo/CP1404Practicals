"""
CP1404/CP5632 - Practical
Practise with reading files
"""

"Question 1."
out_file = open("name.txt", "w")
name = input("Enter name: ")
print(name, file=out_file)
out_file.close()

"Question 2."
in_file = open("name.txt", "r")
name = in_file.read()
in_file.close()
print(f"Your name is {name}")

"Question 3. NOTE: If you wanted to add numbers on line 1 and 10 would you have to give a variable to line 1"
"then read until line 10 then give it a variable? Do lines have an index already assigned to them like characters"
"in a string?"

in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)

"Question 4."
total = 0
in_file = open("numbers.txt", "r")
for line in in_file:
    number = int(line)
    total += line
in_file.close()
print(total)
