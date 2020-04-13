# Write your code here


class CoffeMachine:
    water_available = 400
    milk_available = 540
    coffee_available = 120

    cups_available = 9
    money_available = 550

    def __init__(self):
        while True:
            user_choice = input("Write action (buy, fill, take, remaining, exit): ")
            if user_choice == "buy":
                self.buy()
            elif user_choice == "fill":
                self.fill()
            elif user_choice == "take":
                self.take()
            elif user_choice == "remaining":
                self.remaining()
            elif user_choice == "exit":
                break

    def makeCoffee(self, water, milk, coffee, price):
        if self.water_available >= water and self.coffee_available >= coffee and self.milk_available >= milk \
                and self.cups_available > 1:
            print("I have enough resources, making you a coffee!\n")
            self.water_available -= water
            self.coffee_available -= coffee
            self.milk_available -= milk

            self.cups_available -= 1
            self.money_available += price
        elif water > self.water_available:
            print("Sorry, not enough water!\n")
        elif coffee > self.coffee_available:
            print("Sorry, not enough coffee!\n")
        elif milk > self.milk_available:
            print("Sorry, not enough milk!\n")
        elif 1 > self.cups_available:
            print("Sorry, not enough cups!\n")

    def buy(self):
        coffee_choice = input(
            "\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        if coffee_choice == "1":
            self.makeCoffee(water=250, milk=0, coffee=16, price=4)
        elif coffee_choice == "2":
            self.makeCoffee(water=350, milk=75, coffee=20, price=7)
        elif coffee_choice == "3":
            self.makeCoffee(water=200, milk=100, coffee=12, price=6)

    def fill(self):
        self.water_available += int(input("\nWrite how many ml of water do you want to add: "))
        self.milk_available += int(input("Write how many ml of milk do you want to add: "))
        self.coffee_available += int(input("Write how many grams of coffee beans do you want to add: "))
        self.cups_available += int(input("Write how many disposable cups of coffee do you want to add: "))

    def take(self):
        print(f"I gave you ${self.money_available}")
        self.money_available = 0

    def remaining(self):
        print("\nThe coffee machine has:\n"
              f"{self.water_available} of water\n"
              f"{self.milk_available} of milk\n"
              f"{self.coffee_available} of coffee beans\n"
              f"{self.cups_available} of disposable cups")
        print(f"$" * (self.money_available != 0) + str(self.money_available), "of money\n")


if __name__ == "__main__":
    CoffeMachine()
