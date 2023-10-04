from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def task():
    machine_on = True

    while machine_on:
        order = input("What would you like? latte/espresso/cappuccino: ")

        if order == "report":
            """
            get the resources from the coffee_maker
            get the income from moneymachine
            """
            maker = CoffeeMaker()
            report = maker.report()
            profit = MoneyMachine()
            income = profit.report()

            """
            print the out comes
            """
            print(report)
            print(income)

        elif order == "off":
            machine_on = False
            print("Machine is now shutting down")
        else:
            drink = Menu.find_drink(order)
            if CoffeeMaker.is_resource_sufficient(drink) and MoneyMachine.make_payment(drink.cost):
                CoffeeMaker.make_coffee(drink)


task()
