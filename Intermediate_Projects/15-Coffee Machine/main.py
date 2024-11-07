import art

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    }
}

resources = {
    "water": 600,
    "milk": 400,
    "coffee": 200,
}

machine_money  = 0


def check_ingredients(drink):

    global MENU

    for item in resources:
        if resources[item] < MENU[drink]["ingredients"][item]:
            return False
        else:
            return True

def check_money(drink, money):
    global MENU
    global machine_money

    if money > MENU[drink]["cost"]:
        machine_money += MENU[drink]["cost"]
        process_ingredients(current_order)
        return f"Here is ${round(money - MENU[drink]["cost"], 2)} change.\n Enjoy your {drink}☕."
    elif money == MENU[drink]["cost"]:
        machine_money += MENU[drink]["cost"]
        process_ingredients(current_order)
        return f"Here is your {drink}. Enjoy! ☕."
    else:
        return "Sorry not enough money. Money refunded."

def process_ingredients(drink):
    global MENU
    for item in resources:
        resources[item] -= MENU[drink]["ingredients"][item]

print(art.logo)

while True:
    current_order = input("What would you like? (espresso $1.5 / latte $2.5 / cappuccino $3) ")

    if current_order == "off":
        break
    elif current_order == "report":
        print(resources)
        print(f"Machine has ${machine_money}.")
        continue

    if not check_ingredients(current_order):
        print("Sorry, not enough supplies. Call the staff.")
    else:
        print("Please insert coins.")
        quarters = int(input("How many quarters ")) * 0.25
        dimes = int(input("How many dimes ")) * 0.10
        nickles = int(input("How many nickles ")) * 0.05
        pennies = int(input("How many pennies ")) * 0.01
        current_coins = quarters + dimes + nickles + pennies
        print(check_money(current_order, current_coins))
