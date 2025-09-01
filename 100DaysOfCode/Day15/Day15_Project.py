# Coffee Machine
import data_set as data



def get_report():
    water = data.resources["water"]
    milk = data.resources["milk"]
    coffee = data.resources["coffee"]
    money = data.resources["money"]
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")

def check_avail_resources(selection):
    ingredients = data.MENU[selection]["ingredients"]
    commit = True
    for ing in ingredients:
        if ing != "money" and data.resources[ing] - ingredients[ing] < 0:
            print(f"Sorry there is not enough {ing}")
            commit = False
            break
    return commit
            
def can_pay(selection):
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    cost = data.MENU[selection]["cost"]

    total = quarters*0.25 +  dimes*0.1 + nickles*0.05 +  pennies*0.01

    if total >= cost:
        change = total - cost
        data.resources["money"] += cost
        print(f"Here is ${round(change,2)} in change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def use_resources(selection):
    ingredients = data.MENU[selection]["ingredients"]
    for ing in ingredients:
        if ing == "money":
            data.resources[ing] += ingredients[ing]
        else:
            data.resources[ing] -= ingredients[ing]

def coffee_machine():
    turn_off = False

    while not turn_off:
        selection = input("What would you like? (espresso/latte/cappuccino): ")

        if selection == "off":
            turn_off = True
        elif selection == "report":
            get_report()
        elif selection in data.MENU:
            if check_avail_resources(selection):
                if can_pay(selection):
                     use_resources(selection)
                    

coffee_machine()