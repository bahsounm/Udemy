from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    menu = Menu()
    coffee_machine = CoffeeMaker()
    money_machine = MoneyMachine()
    turn_off = False

    while not turn_off:
        selection = input(f"What would you like? ({menu.get_items()}): ")

        if selection == "off":
            turn_off == True
        elif selection == "report":
            coffee_machine.report()
            money_machine.report()
        elif selection in menu.get_items():
            if coffee_machine.is_resource_sufficient(menu.find_drink(selection)):
                if money_machine.make_payment(menu.find_drink(selection).cost):
                    coffee_machine.make_coffee(menu.find_drink(selection))
coffee_machine()