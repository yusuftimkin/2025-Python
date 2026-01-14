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

def order_check(cust_order, machine_resources):

    if cust_order == "espresso" or cust_order == "latte" or cust_order == "cappuccino":

        if machine_resources["water"] > MENU[cust_order]["ingredients"]["water"] and machine_resources["coffee"] > MENU[cust_order]["ingredients"]["coffee"] and machine_resources["milk"] > MENU[cust_order]["ingredients"]["milk"] :
            return True
        else:
            return False
    else:
        return False


def payment_check(money, cost):
    if money > cost:
        change = money - cost
        resources["money"] += cost
        print(f"Here, your change is ${change}.")
        return True
    elif money == cost:
        resources["money"] += cost
        return True
    else:
        return False


MENU["espresso"]["ingredients"]["milk"] = 0

resources["money"] = 0

order_continue = True

while order_continue:

    customer_order = input("Please enter your order: ").lower()

    if customer_order == "off":
        order_continue = False

    if customer_order == "report":
        print(f"Water: {resources["water"]}")
        print(f"Milk: {resources["milk"]}")
        print(f"Coffee: {resources["coffee"]}")
        print(f"Money: {resources["money"]}")

    order_go = order_check(customer_order, resources)

    if order_go:

        print("Please insert coins: \n")
        quarters = int(input("how many quarters? "))
        dimes = int(input("how many dimes? "))
        nickles = int(input("how many nickles? "))
        pennies =  int(input("how many pennies? "))

        money  =  quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

        if payment_check(money, MENU[customer_order]["cost"]):
            resources["water"] -= MENU[customer_order]["ingredients"]["water"]
            resources["milk"] -= MENU[customer_order]["ingredients"]["milk"]
            resources["coffee"] -= MENU[customer_order]["ingredients"]["coffee"]

            print(f"Here is your {customer_order}. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")
    elif customer_order == "report":
        pass
    else:
        print("Sorry, not enough ingredients")
        order_continue = False
 


