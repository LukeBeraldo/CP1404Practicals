"""
CP1404/CP5632 - Practical
Shop calculator to determine total price of number of items
"""
DISCOUNT_THRESHOLD = 100  # dollars
DISCOUNT_PERCENTAGE = 0.9  # 10% discount

sum_of_items = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    items_price = float(input("Price of item: "))
    sum_of_items += items_price
if sum_of_items > DISCOUNT_THRESHOLD:
    sum_of_items *= DISCOUNT_PERCENTAGE
print(f"Total price for {number_of_items} items is ${sum_of_items:.2f}")
