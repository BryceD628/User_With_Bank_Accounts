class BankAccount:
    def __init__(self, int_rate="1", amount=0):
        self.account_balance = amount
        self.interest_rate = int_rate*.01

    def deposit(self, amount):
        self.account_balance += amount
        print(f"Adding ${amount}. New balance: ${self.account_balance}")
        return self

    def withdraw(self, amount):
        self.account_balance -= amount
        print(f"Withdrawing ${amount}. New balance: ${self.account_balance}")
        return self

    def display_account_info(self):
        print(f"Balance: {self.account_balance}")
        return self

    def yield_interest(self):
        if(self.account_balance > 0):
            self.account_balance += (self.interest_rate * self.account_balance)
            print(f"Interest applied. New balance: {self.account_balance}")
        return self