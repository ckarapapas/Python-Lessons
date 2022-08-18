def legit_input():
    ch = input("What would you like? (espresso/latte/cappuccino):").lower()
    while ch != "espresso" and ch!= "latte" and ch!= "cappuccino" and ch!="off":
        ch = input("Wrong Input: Give again.")
    return ch


function_on = True
while function_on:
    choice = legit_input()
    if choice == "espresso":
        print(choice)
    elif choice == "latte":
        print(choice)

    elif choice == "cappuccino":
        print(choice)

    else:
        function_on = False
