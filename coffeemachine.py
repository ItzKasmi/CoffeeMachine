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


# Function to check for resources
def enough_resources(selected_drink):
    if MENU[selected_drink]["ingredients"]["water"] > resources["water"]:
        print("Sorry, there is not enough water.")
        return False
    elif selected_drink != "espresso" and MENU[selected_drink]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry, there is not enough milk.")
        return False
    elif MENU[selected_drink]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry, there is not enough coffee")
        return False
    else:
        return True


def insert_coins():
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    total_coins = 0.0
    total_coins += (quarters / 4) + (dimes / 10) + (nickles / 20) + (pennies / 100)

    return total_coins


def subtract_resources(selected_drink):
    resources["water"] -= MENU[selected_drink]["ingredients"]["water"]
    if selected_drink != "espresso":
        resources["milk"] -= MENU[selected_drink]["ingredients"]["milk"]
    resources["coffee"] -= MENU[selected_drink]["ingredients"]["coffee"]


# Loop to see if they want more coffee
turn_off = False
while not turn_off:
    choice = input("\nWhat would you like? (Espresso/Latte/Cappuccino): ")
    if choice.lower() == "end":
        turn_off = True

    elif choice.lower() == "report":
        print(f'''
Water: {resources["water"]}
Milk: {resources["milk"]}
Coffee: {resources["coffee"]}
Money: ${"%.2f" % money}
'''
              )

    elif choice.lower() == "espresso":
        espresso = MENU["espresso"]

        if not enough_resources("espresso"):
            pass
        else:
            temp_money = insert_coins()
            if temp_money < espresso["cost"]:
                print("Sorry, you did not pay enough")
            elif temp_money >= espresso["cost"]:
                print(f"Your change is ${"%.2f" % (temp_money - espresso["cost"])}")
                money += espresso["cost"]
                subtract_resources("espresso")
                print("Here is your espresso. Enjoy!")

    elif choice.lower() == "latte":
        latte = MENU["latte"]

        if not enough_resources("latte"):
            pass
        else:
            temp_money = insert_coins()
            if temp_money < latte["cost"]:
                print("Sorry, you did not pay enough")
            elif temp_money >= latte["cost"]:
                print(f"Your change is ${"%.2f" % (temp_money - latte["cost"])}")
                money += latte["cost"]
                subtract_resources("latte")
                print("Here is your latte. Enjoy!")

    elif choice.lower() == "cappuccino":
        cappuccino = MENU["cappuccino"]
        if not enough_resources("cappuccino"):
            pass
        else:
            temp_money = insert_coins()
            if temp_money < cappuccino["cost"]:
                print("Sorry, you did not pay enough")
            elif temp_money >= cappuccino["cost"]:
                print(f"Your change is ${"%.2f" % (temp_money - cappuccino["cost"])}")
                money += cappuccino["cost"]
                subtract_resources("latte")
                print("Here is your cappuccino. Enjoy!")

    else:
        print("Invalid input, try again!")
