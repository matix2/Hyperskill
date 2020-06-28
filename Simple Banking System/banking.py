# Write your code here
from random import sample
import sqlite3


class BankingSystem:
    def __init__(self):
        self.card_data = None
        self.database()

    def menu(self):
        while True:
            print("1. Create an account\n2. Log into account\n0. Exit")
            choice: str = input()
            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.login()
            elif choice == "0":
                print("Bye!")
                exit()
            else:
                print("Unknown option.")

    @staticmethod
    def database(card=None, pin=None, balance=None):
        with sqlite3.connect("card.s3db") as data:
            cursor = data.cursor()
            if not card:
                cursor.execute('''
                CREATE TABLE IF NOT EXISTS card (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                number TEXT NOT NULL UNIQUE,
                pin TEXT NOT NULL,
                balance INTEGER DEFAULT 0 NOT NULL
                );
                ''')
            else:
                cursor.execute('''
                INSERT OR IGNORE INTO card (number, pin, balance)
                VALUES (?, ?, ?);
                ''', (card, pin, balance))

    @staticmethod
    def check_credentials(card):
        with sqlite3.connect("card.s3db") as data:
            cursor = data.cursor()
            cursor.execute('''
            SELECT number, pin, balance FROM card WHERE number = ?;
            ''', (card,))
            return cursor.fetchone()

    @staticmethod
    def add_income(card):
        income = input("Enter income:\n")
        with sqlite3.connect("card.s3db") as data:
            cursor = data.cursor()
            cursor.execute(f'''
                        UPDATE card SET balance = balance + ? WHERE number = ?;
                        ''', (income, card))
            print("Income was added!\n")
            return cursor.fetchone()

    @staticmethod
    def do_transfer(card):
        transfer_card = input("Enter card number:\n")
        if BankingSystem.luhn_algorithm(transfer_card):
            with sqlite3.connect("card.s3db") as data:
                cursor = data.cursor()
                cursor.execute('''
                SELECT number FROM card WHERE number = ?;
                ''', (transfer_card,))
                row = cursor.fetchone()

                if row is None:
                    print("Such a card does not exist.")
                else:
                    amount = int(input("Enter how much money you want to transfer:\n"))
                    cursor.execute('''
                    SELECT balance FROM card WHERE number LIKE (?);
                    ''', (card,))
                    row2 = cursor.fetchone()[0]
                    if int(amount) > row2:
                        print("Not enough money!")
                    else:
                        cursor.execute(f'''
                                        UPDATE card SET balance = balance + ? WHERE number = ?;
                                        ''', (amount, transfer_card))
                        cursor.execute(f'''
                                        UPDATE card SET balance = balance - ? WHERE number = ?;
                                        ''', (amount, card))
                        print("Success!")

                return cursor.fetchone()
        else:
            print("Probably you made mistake in the card number. Please try again!")

    @staticmethod
    def close_account(card):
        with sqlite3.connect("card.s3db") as data:
            cursor = data.cursor()
            cursor.execute(f'''
                        DELETE FROM card WHERE number = ?;
                        ''', (card,))
            return cursor.fetchone()

    @staticmethod
    def luhn_algorithm(card_number):
        number = [int(i) for i in card_number]
        for x, num in enumerate(number):
            if (x + 1) % 2 == 0:
                continue
            n = num * 2
            number[x] = n if n < 10 else n - 9
        return sum(number) % 10 == 0

    @staticmethod
    def generate_numbers():
        while True:
            random_card = ''.join(["400000"] + [str(n) for n in sample(range(9), 9)] + ["7"])
            random_pin = ''.join([str(n) for n in sample(range(9), 4)])
            if not BankingSystem.check_credentials(random_card):
                if BankingSystem.luhn_algorithm(random_card):
                    yield random_card, random_pin
            else:
                continue

    def create_account(self):
        card, pin = next(self.generate_numbers())
        self.database(card, pin, 0)
        print("\nYour card has been created")
        print(f"Your card number:\n{card}")
        print(f"Your card PIN:\n{pin}\n")

    def login(self):
        card: str = input("Enter your card number:\n")
        pin: str = input("Enter your PIN:\n")
        try:
            self.card_data = self.check_credentials(card)
            if self.card_data[1] == pin:
                print("You have successfully logged in!\n")
                self.account()
            else:
                print("Wrong card number or PIN\n")
        except (KeyError, TypeError):
            print("Wrong card number or PIN\n")

    def account(self):
        while True:
            print("1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit")
            choice = input()
            if choice == "1":
                print(f"\nBalance: {self.card_data[2]}\n")
            elif choice == "2":
                self.add_income(self.card_data[0])
            elif choice == "3":
                self.do_transfer(self.card_data[0])
            elif choice == "4":
                self.close_account(self.card_data[0])
            elif choice == "5":
                self.card_data = None
                print("You have successfully logged out!\n")
                return
            elif choice == "0":
                print("Bye!")
                exit()
            else:
                print("Unknown option.\n")


BankingSystem().menu()
