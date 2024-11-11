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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def checking_resources(order_ingredients):
    water_amount = order_ingredients['water']
    milk_amount = order_ingredients.get('milk', 0)
    coffee_amount = order_ingredients['coffee']
    if resources['water'] < water_amount or resources['milk'] < milk_amount or resources['coffee'] < coffee_amount:
        print("Sorry there is not enough water.")
        return False
    else:
        return True

def coin_processing():
        print("Please insert coins.")
        quarters = int(input("how many quarters?"))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
        total= quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
        return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change}")
        print(f'Here is your {option} ☕️. Enjoy!')
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def removing_resources(order_ingredients):
    for ingredient, amount in order_ingredients.items():
        if ingredient == 'water':
            resources[ingredient] -= order_ingredients[ingredient]
        elif ingredient == 'milk':
            resources[ingredient] -= order_ingredients[ingredient]
        else:
            resources[ingredient] -= order_ingredients[ingredient]

turn_off = False
profit = 0
while not turn_off:
    option = input("What would you like? (espresso/latte/cappuccino).\nType 'report' to see the amount of ingredients available. ")
    if option == 'report'.lower():
        for resource in resources:
            if resource == 'coffee':
                print(f'{resource}: {resources[resource]}g')
            else:
                print(f'{resource}: {resources[resource]}ml')
        print(f"Money: ${profit}")
    elif option == 'off':
         turn_off = True
    else:
        drink = MENU[option]
        if checking_resources(drink['ingredients']):
            payment = coin_processing()
            if is_transaction_successful(payment, drink['cost']):
                removing_resources(drink['ingredients'])



