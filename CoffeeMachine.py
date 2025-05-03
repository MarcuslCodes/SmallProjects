# <>\
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
    "money": 0,
}


#check how much money the user has and then show what the user can afford. Check the balance and resources.

quarters = 0.25
dime = 0.10
nickle = 0.05
penny = 0.01

def insert_coin():
    int(input("How many quarters? "))
    int(input("How many dimes? "))
    int(input("How many nickles? "))
    int(input("How many pennies? "))

def coffe_type(user_choice):
    if user_choice == 'espresso':
        print("Please insert coins!")
        insert_coin()
    elif user_choice == 'latte':
        print("Please insert coins!")
        insert_coin()
    elif user_choice == 'cappuccino':
        print("Please insert coins!")
        insert_coin()


def machine_report():
    for item, amount in resources.items():
        if item == "money":
            print(f"{item}: ${amount}")
        elif item in ["water", "milk"]:
            print(f"{item}: {amount}ml")
        elif item == "coffee":
            print(f"{item}: {amount}g")

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


user_ordering = True

while user_ordering:

    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if user_choice == "report":
        machine_report()

    if user_choice == "off":
        print(f"Machine is now turned off! Final count is ${resources["money"]}")
        machine_report()

    coffe_type(user_choice)
