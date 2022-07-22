# --------------------------------------------------------
# -------------------- COFFEE MAKER ----------------------
# --------------------------------------------------------


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

moneyCollected = 0
titleList = list(MENU.keys())
menuItems = '/'.join(titleList)


def report():
    """Generates the report"""
    print(f"----------\n"
          f"Remaining: \n"
          f"Water: {resources['water']}ml \n"
          f"Milk: {resources['milk']}ml \n"
          f"Coffee: {resources['coffee']}g \n"
          f"Money: ${moneyCollected} \n"
          f"----------")


def putCoins(money):
    """Processes the coins inserted into the coffee machine & gives coffee"""
    global moneyCollected
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    totalMoney = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    print(f"Total Coins: {totalMoney}")
    if totalMoney < money:
        print("Sorry that's not enough money. Money refunded.")
    elif totalMoney >= money:
        resources['water'] -= reqWater
        resources['milk'] -= reqMilk
        resources['coffee'] -= reqCoffee
        moneyCollected += money
        print(f"Here is your {prompt}. Enjoy!")
    if totalMoney > money:
        balance = (totalMoney - money).__round__(2)
        print(f"Here is ${balance} dollars in change.")


def checkResources(water, milk, coffee, money):
    """Checks for resources before making coffee"""
    if resources['water'] - water < 0:
        print("Sorry there is not enough water.")
        return False
    if resources['milk'] - milk < 0:
        print("Sorry there is not enough milk.")
        return False
    if resources['coffee'] - coffee < 0:
        print("Sorry there is not enough coffee.")
        return False
    else:
        putCoins(money)
        return True


while True:
    prompt = input(f"What would you like? ({menuItems}):").lower()
    if prompt == 'latte':
        reqWater = 50
        reqMilk = 0
        reqCoffee = 18
        reqMoney = 1.50
        checkResources(reqWater, reqMilk, reqCoffee, reqMoney)

    elif prompt == 'espresso':
        reqWater = 200
        reqMilk = 150
        reqCoffee = 24
        reqMoney = 2.50
        checkResources(reqWater, reqMilk, reqCoffee, reqMoney)

    elif prompt == 'cappuccino':
        reqWater = 250
        reqMilk = 100
        reqCoffee = 24
        reqMoney = 3.00
        checkResources(reqWater, reqMilk, reqCoffee, reqMoney)

    elif prompt == 'report':
        report()

    elif prompt == 'off':
        print("Powering off.")
        break
