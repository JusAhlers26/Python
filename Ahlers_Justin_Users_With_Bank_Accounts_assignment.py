class Bank_Acc:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print(f"Insufficient funds: Charging a $3 fee")
            self.balance -= 3
        return self

    def display_account_info(self):
        return f"{self.balance}"

    def yield_interest(self):
        if self.balance >= 0:
            self.balance += (self.balance * self.int_rate)
        return self

class User:

    def __init__(self, name):
        self.name = name
        self.account = (Bank_Acc(.01, 2600))

    def display_user_balance(self):
        print(f"user: {self.name}, Balance: {self.account.display_account_info()}")
        return self

    def trans_mon(self, user, amount):
        user.amount += amount
        self.amount -= amount
        user.disp_user_bal()
        self.disp_user_bal()
        return self

justin = User("Justin Ahlers")
justin.account.deposit(1300)
justin.disp_user_bal()