# Write your code here

# Starting State
water_amount = 400
milk_amount = 540
beans_amount = 120
cups_amount = 9
money_amount = 550
make_coffee = True

# Functions


def print_state():
    print("The coffee machine has:")
    print(str(water_amount) + " of water")
    print(str(milk_amount) + " of milk")
    print(str(beans_amount) + " of coffee beans")
    print(str(cups_amount) + " of disposable cups")
    print(str(money_amount) + " of money")


def check_ingredient_amounts(coffee_selection):
    global make_coffee
    if coffee_selection == "1":
        if water_amount < 250 or beans_amount < 16 or cups_amount < 1:
            print("I don't have enough resources to make you coffee.")
            make_coffee = False
        else:
            print("I have enough resources, making you a coffee!")
            make_coffee = True
    elif coffee_selection == "2":
        if water_amount < 350 or beans_amount < 20 or milk_amount < 75 or cups_amount < 1:
            print("I don't have enough resources to make you coffee.")
            make_coffee = False
        else:
            print("I have enough resources, making you a coffee!")
            make_coffee = True
    elif coffee_selection == "3":
        if water_amount < 200 or beans_amount < 12 or milk_amount < 100 or cups_amount < 1:
            print("I don't have enough resources to make you coffee.")
            make_coffee = False
        else:
            print("I have enough resources, making you a coffee!")
            make_coffee = True
    else:
        pass


def buy_function():
    global water_amount
    global milk_amount
    global beans_amount
    global cups_amount
    global money_amount
    global make_coffee
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    coffee_selection = input()
    check_ingredient_amounts(coffee_selection)
    if coffee_selection == "1" and make_coffee == True:
        water_amount -= 250
        beans_amount -= 16
        cups_amount -= 1
        money_amount += 4
    elif coffee_selection == "2" and make_coffee == True:
        water_amount -= 350
        milk_amount -= 75
        beans_amount -= 20
        cups_amount -= 1
        money_amount += 7
    elif coffee_selection == "3" and make_coffee == True:
        water_amount -= 200
        milk_amount -= 100
        beans_amount -= 12
        cups_amount -= 1
        money_amount += 6
    else:
        pass


def fill_function():
    global water_amount
    global milk_amount
    global beans_amount
    global cups_amount
    print("Write how many ml of water you want to add:")
    water_amount += int(input())
    print("Write how many ml of milk you want to add:")
    milk_amount += int(input())
    print("Write how many grams of coffee beans you want to add:")
    beans_amount += int(input())
    print("Write how many disposable coffee cups you want to add:")
    cups_amount += int(input())


def take_function():
    global money_amount
    print("I gave you $" + str(money_amount))
    money_amount = 0

# Execution

class coffeeMachine:
    def __init__(self):
        self.state = "choosing an action"
        self.machine_input()

    def machine_input(self):
        print("Write action (buy, fill, take, remaining, exit):")
        user_input = input()
        self.process(user_input)

    def process(self, user_input):
        if user_input == "buy":
            buy_function()
            coffeeMachine()
        elif user_input == "fill":
            fill_function()
            coffeeMachine()
        elif user_input == "take":
            take_function()
            coffeeMachine()
        elif user_input == "remaining":
            print_state()
            coffeeMachine()


coffeeMachine()
