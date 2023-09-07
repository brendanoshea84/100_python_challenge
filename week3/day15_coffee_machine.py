# 3 hot flavors
flavours = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.50
    },

    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
        },
        "cost": 2.50
    },

    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 190,
        },
        "cost": 3.50
    },
}
# Machine resources
Machine = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

profit = 0
#
coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}


machine_on = True


def transation_successful(money_recieved, drink_cost):
    """
    Return TRUE if coins is more than drink cost
    """
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is your change: ${change} ")
        global profit
        profit += drink_cost
        return True
    else:
        print("Not enough money")
        return False


def make_coffee(drink_name, order_ingred):
    """
    deduct the ingrediants from resources
    """
    for item in order_ingred:
        Machine[item] -= order_ingred[item]
    print(f"Here is your {drink_name}")


def resoucrse(order_in):
    """
    return True if resources are aviable
    """
    for item in order_in:
        if order_in[item] >= Machine[item]:
            print(f"Sorry there isnt enough {item}")
            return False
    return True


def process_coins():
    """
    Return total calcualtions of coins inserted
    """
    print("Please insert coins")
    total = int(input("how many quarters ")) * .25
    total += int(input("how many dime ")) * .10
    total += int(input("how many nickel ")) * .05
    total += int(input("how many penny ")) * .01
    return total


while machine_on:
    task = input("What would you like ? espresso/latte/cappuccino ")

    if task == "off":
        machine_on = False

    elif task == "report":
        print(f"water: {Machine['water']} ml")
        print(f"milk: {Machine['milk']} ml")
        print(f"coffee: {Machine['coffee']} grams")
        print(f"money: ${profit}")

    else:
        drink = flavours[task]
        if resoucrse(drink["ingredients"]):
            payment = process_coins()
            if transation_successful(payment, drink["cost"]):
                make_coffee(task, drink["ingredients"])
