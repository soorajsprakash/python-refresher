from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


myCoffeeMaker = CoffeeMaker()
myMoneyMachine = MoneyMachine()
myMenu = Menu()

isOn = True

while isOn:
    drinkMenu = myMenu.get_items()
    prompt = input(f"What would you like? ({drinkMenu}): ")

    if prompt == 'report':
        myCoffeeMaker.report()
        myMoneyMachine.report()
    elif prompt == 'off':
        print("Shutting down.")
        isOn = False
    else:
        myDrink = myMenu.find_drink(prompt)
        if myCoffeeMaker.is_resource_sufficient(myDrink) and myMoneyMachine.make_payment(myDrink.cost):
            print(f"have res to make ur {prompt}")
            myCoffeeMaker.make_coffee(myDrink)
