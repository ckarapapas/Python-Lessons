def legit_input():
    ch = input("What would you like? (espresso/latte/cappuccino): ").lower()
    while ch != "espresso" and ch != "latte" and ch != "cappuccino" and ch != "off" and ch != "report":
        ch = input("Wrong Input: Give again.")
    return ch


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
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def checkforsuf(ch):
    if MENU[ch]["ingredients"]["milk"] <= resources["milk"]:
        if MENU[ch]["ingredients"]["water"] <= resources["water"]:
            if MENU[ch]["ingredients"]["coffee"] <= resources["coffee"]:
                f = ""
            else:
                f = "coffee"
        else:
            f = "water"
    else:
        f="milk"
    return f


def money():
    q = int(input("How many quarters"))
    d = int(input("How many dimes"))
    n = int(input("How many nickles"))
    p = int(input("How many pennies"))
    su = q * 0.25 + d * 0.10+ n * 0.05 + p*0.01
    return su


function_on = True

while function_on:
    choice = legit_input()
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        flag = checkforsuf(choice)
        if flag == "":
            amount = money()
            if amount >= MENU[choice]["cost"]:
                print("Here is your change", round(amount - MENU[choice]["cost"], 2))
                resources["money"] += MENU[choice]["cost"]
                resources["water"] -= MENU[choice]["ingredients"]["water"]
                resources["milk"] -= MENU[choice]["ingredients"]["milk"]
                resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
                print(f"Here is your {choice}, enjoy!")
            else:
                print("Sorry that's not enough money, money refunded!")
        else:
            print(f"Not enough resources, we are out of {flag}.")

    elif choice == "report":
        print(resources)
    else:
        function_on = False


