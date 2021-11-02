from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo


def pick_drink(menu, cm, mm):
    """
    retrieves user's input for drink/action for machine to take
    :return: string - keyword for drink/action that user selects
    """
    while True:
        choice = input(f"What would you like? {menu.get_items()[:-1]}: ").lower()
        if choice == "off":
            return 'off'
        elif choice == "report":
            cm.report()
            mm.report()
            break
        elif drink := menu.find_drink(choice):
            return drink
        else:
            print("Please choose one of the three provided options.\n")


def run_machine():
    """
    Runs the coffee machine
    """
    print(logo)
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()
    while (drink := pick_drink(menu, coffee_maker, money_machine)) != 'off':
        if drink and coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
        print('\n')


if __name__ == "__main__":
    run_machine()