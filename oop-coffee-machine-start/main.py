from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def legit_input():
    ch = input(f"What would you like? {menu.get_items()}: ").lower()
    while ch != "espresso" and ch != "latte" and ch != "cappuccino" and ch != "off" and ch != "report":
        ch = input("Wrong Input: Give again.")
    return ch


menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()


function_on = True
while function_on:
    choice = legit_input()
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        function_on = False
    else:
        drink = menu.find_drink(choice)
        f  = coffee_maker.is_resource_sufficient(drink)
        if f:
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)



