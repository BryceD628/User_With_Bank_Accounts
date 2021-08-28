from bankAccount import BankAccount


class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount(amount=0, int_rate=0.02)

    def makeDeposit(self, deposit_amount):
        self.account.deposit(deposit_amount)
        return self

    def makeWithdrawal(self, withdrawal_amount):
        self.account.withdraw(withdrawal_amount)
        return self

    def displayUserBalance(self):
        self.account.display_account_info()
        return self


jeff = User("Jeff", "jeff@dojo.com")
chad = User("Chad", "bigbro@family.com")
giannis = User("Giannis", "greekgod@nba.com")

jeff.makeDeposit(12).makeDeposit(1).makeDeposit(1000).makeWithdrawal(11).displayUserBalance()

chad.makeDeposit(150).makeDeposit(399).makeWithdrawal(20).makeWithdrawal(100).displayUserBalance()

giannis.makeDeposit(25000).makeWithdrawal(4).makeWithdrawal(8).makeWithdrawal(135).displayUserBalance()