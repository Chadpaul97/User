
class User:
    def __init__(self, fname, lname, age, email):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.email = email
        self.account_balance = 0

    def make_deposit(self,amount):
        self.account_balance += amount

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        self.account_balance

    def transfer_money(self,amount, user):
        self.account_balance -= amount
        user.account_balance += amount
        return user

andre = User("Andre", "Dion", 39, "andre@email.com")
ryan = User("Ryan", "Door", 49, "ryan@email.com")
jessica = User("Jessica", "loop", 83, "jessica@email.com")

# Have the first user make 3 deposits and 1 withdrawal and then display their balance
andre.make_deposit(100)
andre.make_deposit(100)
andre.make_deposit(100)
andre.make_withdrawl(75)
print(andre.account_balance)

# Have the second user make 2 deposits and 2 withdrawals and then display their balance
ryan.make_deposit(200)
ryan.make_deposit(1000)
ryan.make_withdrawl(25)
ryan.make_withdrawl(300)
print(ryan.account_balance)

# Have the third user make 1 deposits and 3 withdrawals and then display their balance
jessica.make_deposit(1500)
jessica.make_withdrawl(300)
jessica.make_withdrawl(300)
jessica.make_withdrawl(300)
print(jessica.account_balance)

# BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances
andre.transfer_money(300,jessica)
print(andre.account_balance)
print(jessica.account_balance)