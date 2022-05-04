class account():
    def __init__(self,owner,start_balance=0):
        self.owner = owner
        self.start_balance = start_balance
        self.balance = self.start_balance

    def deposit(self,ammount):
        self.ammount = ammount
        self.balance += self.ammount

    def withdrawal(self,amm):
        self.amm = amm
        if self.amm <= self.balance:
            self.balance -= self.amm
        else :
            print(f"There is only {self.balance} on the account")


    def __str__(self):
        return f"The owner of the account is {self.owner}\n" \
               f"There is {self.balance} on the account"


ac1 = account("Bartek",500)
ac1.withdrawal(300)
ac1.deposit(600)
ac1.deposit(500)
ac1.deposit(600)
ac1.withdrawal(400)
ac1.withdrawal(1600)
print(ac1)