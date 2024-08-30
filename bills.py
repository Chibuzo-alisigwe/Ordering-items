"""This code will provide the total cost of breakfast in an English eatry"""

foods = ["Eggs", "Tomatoes", "Baked beans", "Bacon", "Sausages"]   # List of items available for breakfast

# A dictionaery showing the price of each item on the list
prices = {
    "Eggs" : 10,
    "Tomatoes" : 4,
    "Baked beans" : 5,
    "Bacon" : 7,
    "Sausages" : 5.50
}

UserOrder = {}

for items in prices.keys():
    quantity = int(input(f"How many {items} do you want to buy?"))
    UserOrder[items] = quantity

print(UserOrder)
    