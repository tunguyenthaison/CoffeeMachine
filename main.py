# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


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
#
# current_data = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
#     "profit": 0
# }
#
# MONEY = {
#     "quarters": 21,
#     "dimes": 1,
#     "nickles": 2,
#     "pennies": 57
# }


def computeMoney(MONEY):
    pennies_total = MONEY['pennies'] + 5*MONEY['nickles'] + 10*MONEY['dimes'] + 25*MONEY['quarters']
    dollars_total = pennies_total//100
    remaining = pennies_total - dollars_total*100
    return dollars_total + remaining/100



def checkMoney(MONEY, choice):
    """
    :param MONEY: the amount of money the user put in
    :param choice: espresso/latte/cappuccino
    :return: [TRUE, refund] or [FALSE, refund]
    """
    choice_item = MENU[choice]
    cost_item = choice_item['cost']
    if computeMoney(MONEY) < cost_item:
        return [False, computeMoney(MONEY)]
    else:
        refund = computeMoney(MONEY) - cost_item
        if refund > 0:
            return [True, refund]




def makeCoffee(current_data, choice):
    current_data['profit'] += MENU[choice]['cost']
    needed_things =  MENU[choice]["ingredients"]
    for x in needed_things:
        current_data[x] -= needed_things[x]
    print(f"Here is your {choice} ☕. Enjoy!")



def print_report_online(current_data, MONEY):
    print(f"Water: {current_data['water']}ml")
    print(f"Milk: {current_data['milk']}ml")
    print(f"Coffee: {current_data['coffee']}g")
    print(f"Money: ${computeMoney(MONEY)}")
    return

def print_report_check(current_data):
    print(f"Water: {current_data['water']}ml")
    print(f"Milk: {current_data['milk']}ml")
    print(f"Coffee: {current_data['coffee']}g")
    print(f"Money: ${current_data['profit']}")
    return

def checkResources(current_data, choice):
    """
    :param choice: espresso/latte/cappuccino
    :return: True/False depending on the resources available (not checking money)
    """
    choice_item = MENU[choice]
    ingred_item = choice_item['ingredients']
    for x in ingred_item:
        if ingred_item[x] > current_data[x]:
            print(f"Sorry there is not enough {x}.")
            return False
    return True


def turnOff():
    print("Machine is turning off!")
    return

def insertCoin(MONEY):
    print("Please insert coins.")
    for x in MONEY:
        MONEY[x] = int(input(f"How many {x}?: "))



def CoffeeMachine():

    # Initiate the current data of the machine
    current_data = resources.copy()
    current_data['profit'] = 0

    # Initiate the MONEY
    MONEY = {
        "quarters": 0,
        "dimes": 0,
        "nickles": 0,
        "pennies": 0
    }

    # Run the machine
    # Make it repeatable later
    is_On = True
    while is_On:
        print("---------------------------------------------------------------")
        choice = input("    What would you like? (espresso/latte/cappuccino): ").lower()
        # Process to turn of the machine
        if choice == "off":
            is_On = False
            turnOff()
            return
        # End of the process to turn of the machine

        elif choice == "report":
            print_report_check(current_data)
            continue

        # Process the right keyword entered
        elif choice not in ["espresso", 'latte', 'cappuccino']:
            print("Invalid choice! Please enter again.")
            continue
        # End of the process the right keyword entered

        else:

            # Insert coins
            insertCoin(MONEY)
            # print_report_online(current_data, MONEY)

            # Check resources
            is_EnoughStuff = checkResources(current_data, choice)

            if is_EnoughStuff == False:
                continue
                # do nothing
            else:
                # Check money
                is_EnoughMoney = checkMoney(MONEY, choice)[0]
                refund = checkMoney(MONEY, choice)[1]
                if is_EnoughMoney == False:
                    print("Sorry that is not enough money. Money refunded.")
                else:
                    print(f"Here is ${refund:.2f} dollars in change.")
                    makeCoffee(current_data, choice)



CoffeeMachine()

# TODO: 1. Print the report of resources.
# TODO: 2. Check resources sufficient to make drink order.
# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”