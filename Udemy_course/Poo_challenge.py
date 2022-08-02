class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Owner: {self.owner} \nBalance: {self.balance}"

    def deposit(self, amount):
        print("Deposit Accepted")
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance > amount:
            print("Withdraw Accepted")
            self.balance = self.balance - amount
        else:
            print("Funds Unavailable!")


acct1 = Account('Jose', 100)
print(acct1)

print(acct1.owner)

print(acct1.balance)

acct1.deposit(50)

acct1.withdraw(75)

print(acct1)
acct1.withdraw(500)
