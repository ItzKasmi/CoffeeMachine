from data import MENU, resources

"""
Make 3 hot flavors
- Water
- Coffee
- Milk

Use Coins
- Penny: 1
- Nickel: 5
- Dime: 10
- Quarter: 25
"""

# Keep track of total money
money = 0.0

# Loop to see if they want more coffee
turn_off = False
while not turn_off:
    choice = input("What would you like? (Espresso/Latte/Cappuccino): ")
    if choice.lower() == "end":
        turn_off = True

    elif choice.lower() == "report":
        print(f'''
Water: {resources["water"]}
Milk: {resources["milk"]}
Coffee: {resources["coffee"]}
Money: ${money}
'''
        )

    elif choice.lower() == "espresso":
        pass

    elif choice.lower() == "latte":
        pass

    elif choice.lower() == "cappuccino":
        pass

    else:
        print("Invalid input")
