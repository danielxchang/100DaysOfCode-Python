from machine_data import logo, resources, MENU


def display_report():
    """
    displays the resources of the coffee machine at the given moment
    """
    print(f"Water: {resources['water']}ml\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money: ${resources['money']}")


def get_drink_ingredients(drink):
    """
    retrieves the dictionary of ingredients for a drink
    :param drink: string representing key of MENU dictionary
    :return: dictionary of ingredients for drink
    """
    return MENU[drink]['ingredients']


def enough_resources(drink):
    """
    checks if machine has enough resources to make drink
    :param drink: string of requested drink
    :return: True or False
    """
    for ingredient, amount in get_drink_ingredients(drink).items():
        if resources[ingredient] < amount:
            print(f"Sorry there is not enough {ingredient}.")
            return False

    return True


def make_drink(drink):
    """
    updates the resource dictionary after making cup of coffee
    :param drink: string drink to be made
    """
    for ingredient, amount in get_drink_ingredients(drink).items():
        resources[ingredient] -= amount

    resources['money'] += MENU[drink]['cost']


def enter_coins():
    """
    retrieves amount of coins from user
    :return: int quantity of each coin
    """
    while True:
        try:
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickels = int(input("How many nickels? "))
            pennies = int(input("How many pennies? "))
            break
        except ValueError:
            print("Please enter the number of coins.")

    return quarters, dimes, nickels, pennies


def process_coins():
    """
    processes the coins and returns the total
    :return: float - sum of all coins
    """
    print("Please insert coins.")
    quarters, dimes, nickels, pennies = enter_coins()
    return (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickels) + (0.01 * pennies)


def pick_drink():
    """
    retrieves user's input for drink/action for machine to take
    :return: string - keyword for drink/action that user selects
    """
    while True:
        drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if drink in ['off', 'espresso', 'latte', 'cappuccino', 'report', 'restock', 'withdraw']:
            return drink
        else:
            print("Please choose one of the three provided options.")


def restock():
    """
    restocks a resource based off user's inputs
    """
    while True:
        if (resource := input("Enter which resource to restock ('water', 'milk', or coffee'): ").lower()) \
                not in ['water', 'milk', 'coffee']:
            print('Please enter one of the three resources.')
            continue
        try:
            quantity = int(input("Enter the quantity (ml or g) of the resource to be restocked: "))
            resources[resource] += quantity
            break
        except ValueError:
            print('Please enter an integer for the quantity to be restocked.')


def withdraw():
    """
    withdraws money from the amount in the resources dictionary
    """
    while True:
        try:
            amt = round(float(input("Enter the amount of money to withdraw: $")), 2)
            if (money := resources['money']) < amt:
                print(f"The withdrawal amount of ${amt} is more than the ${money} in the machine.")
                continue
            resources['money'] -= amt
            break
        except ValueError:
            print('Please enter a number for the withdrawal amount.')


def start_machine():
    """
    primary function representing the coffee machine
    """
    print(logo)
    while (drink := pick_drink()) != 'off':
        if drink == 'report':
            display_report()
        elif drink == 'restock':
            restock()
        elif drink == 'withdraw':
            withdraw()
        else:
            if enough_resources(drink):
                amt_paid = process_coins()
                if (change := amt_paid - MENU[drink]['cost']) < 0:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    make_drink(drink)

                    print(f"Here is ${round(change, 2)} in change.")
                    print(f"Here is your {drink} ☕️. Enjoy!")
        print('\n')


if __name__ == "__main__":
    start_machine()
