from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu ()
coffee = CoffeeMaker()
moneymachine = MoneyMachine()
machineoff = False

while not machineoff:
    choice = input(f"What would you like? ({menu.get_items()}): ")

    if choice == "off":
        machineoff = True

    elif choice == "report":
        coffee.report()
        moneymachine.report()

    else:
        drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(drink):
            if moneymachine.make_payment(drink.cost):
                coffee.make_coffee(drink)
