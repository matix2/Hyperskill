import math
import argparse
import numbers


class CreditCalculator:
    def __init__(self, interest, calc_type, principal, periods, payment):
        self.type = calc_type
        self.principal = principal
        self.payment = payment
        self.periods = periods
        self.interest = interest if interest is None else interest / (100 * 12)
        self.overpayment = 0

    def get_additional(self):
        return self.interest * (1 + self.interest) ** self.periods / ((1 + self.interest) ** self.periods - 1)

    def get_overpayment(self, all_payment=0):
        if self.type == "diff":
            return all_payment - self.principal
        return self.payment * self.periods - self.principal

    def get_period(self):
        self.periods = math.ceil(
            math.log(self.payment / (self.payment - self.interest * self.principal),
            (1 + self.interest))
        )
        self.overpayment = self.get_overpayment()
        return f"You need {self.months_to_years()} to repay this credit!\nOverpayment = {self.overpayment}"

    def get_diff_payment(self):
        all_payments = 0
        for month in (number + 1 for number in range(self.periods)):
            diff_pay = math.ceil(
                self.principal / self.periods + self.interest * (
                        self.principal - self.principal * (month - 1) / self.periods)
            )
            all_payments += diff_pay
            print(f"Month {month}: paid out {diff_pay}")
        return f"Overpayment = {self.get_overpayment(all_payments)}"

    def get_ann_payment(self):
        self.payment = math.ceil(
            self.principal * (
                    (self.interest * (1 + self.interest) ** self.periods) /
                    ((1 + self.interest) ** self.periods - 1)
            )
        )
        return f"Your annuity payment = {self.payment}!"

    def get_principal(self):
        self.principal = math.floor(
            self.payment / (
                    (self.interest * (1 + self.interest) ** self.periods) /
                    ((1 + self.interest) ** self.periods - 1)
            )
        )
        self.principal = int(self.payment / self.get_additional())
        self.overpayment = self.get_overpayment()
        return f"Your credit principal = {self.principal}\nOverpayment = {self.overpayment}"

    def months_to_years(self):
        result = ""
        years = self.periods // 12
        months = self.periods % 12

        if years:
            result += f"{years} year"
            if years % 10 != 1 or years == 11:
                result += "s"

        if years and months:
            result += " and "

        if months:
            result += f"{months} month"
            if months > 1:
                result += "s"
        return result

    def check_state(self):
        lst = [self.type, self.principal, self.periods, self.payment]
        if self.interest is None or lst.count(None) != 1 or \
                any([elem < 0 for elem in lst if isinstance(elem, numbers.Number)]):
            return False
        return True

    def calculate(self):
        if not self.check_state():
            return "Incorrect parameters"

        if self.periods is None:
            return self.get_period()
        if self.principal is None:
            return self.get_principal()
        if self.payment is None:
            if self.type == "diff":
                return self.get_diff_payment()
            return self.get_ann_payment()

        return "Impossible output by task condition!"

    def run(self):
        print(self.calculate())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", type=str)
    parser.add_argument("--principal", type=int)
    parser.add_argument("--periods", type=int)
    parser.add_argument("--interest", type=float)
    parser.add_argument("--payment", type=int)

    args = parser.parse_args()
    params = [args.interest, args.type, args.principal,
              args.periods, args.payment]

    calculator = CreditCalculator(*params)
    calculator.run()
