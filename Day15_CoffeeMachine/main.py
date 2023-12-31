MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

current_funds = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(order_ingredients):
    """Returns true when order can be fufilled, False if machine does not have enough resources"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, please refill the [item] before ordering.")
            return False
    return True


# this part seems kind of silly but is important to the project as a whole and i guess we GOTTA
def coin_input():
    """Returns the total from coins inserted"""
    print("Please insert coins")
    total = int(input("how many dollars?: ")) * 1.0
    total += int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def transaction(money_received, drink_cost):
    """Return True when the payment is accepted, or False if funds are insufficient."""
    if money_received >= drink_cost:
        change_dispensed = round(money_received - drink_cost, 2)
        print(f"Here is your change: ${change_dispensed}")
        global currentFunds
        current_funds += drink_cost
        return True
    else:
        print("Sorry, thats an insufficient amount of funds. Money has been refunded.")
        return False


def make_order(drink_name, order_ingredients):
    """Subtracts the required ingredients from the total resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


coffe_machine_on = True
while coffe_machine_on:
    choice = input(
        "Hello, what would you like to order?\n Espresso Shot: $1.50\n Latte: $2.50\n Cappuccino: $3.00 \nPlease type in the item you would like to order: "
    ).lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${current_funds}")
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = coin_input()
            if transaction(payment, drink["cost"]):
                make_order(choice, drink["ingredients"])
