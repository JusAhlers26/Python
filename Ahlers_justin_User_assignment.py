class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_dep(self, amount):
        self.amount += amount
        return self

    def make_withd(self, amount):
        self.amount += amount
        return self

    def disp_user_bal(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def trans_mon(self, user, amount):
        user.amount += amount
        self.amount -= amount
        user.disp_user_bal()
        self.disp_user_bal()

justin = User("Justin Ahlers")
vy = User("Vy Ahlers")
eliana = User("Elian Ahlers")

justin.make_dep(1790).make_dep(50).make_dep(1790).make_withd(1100).disp_user_bal()
vy.make_dep(700).make_dep(200).make_withd(350).make_withd(400).disp_user_bal()
eliana.make_dep(900).make_withd(50).make_withd(40).make_withd(200).disp_user_bal()