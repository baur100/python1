

class Bank ():
    name_on_account = ""
    deposit = 0
    withdraw = 0
    balance = 0


    def get_balance (self):
        return self.balance - self.withdraw or self.balance + self.deposit

    def print_info (self):
        print ( f" name on account - {self.name_on_account} ")
        print (f"your balance is - {self.balance }")
