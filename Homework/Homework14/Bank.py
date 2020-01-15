

class Bank:
    # first_name_on_account = ""
    # second_name_on_account = ""
    # balance = 0
    # all_accounts = []


    def __init__(self,first_name_on_account, second_name_on_account, balance ,all_accounts):
        self.first_name_on_account = first_name_on_account
        self.second_name_on_account =second_name_on_account
        self.balance =balance
        self.all_accounts =all_accounts

    def __repr__(self):
        return (f"{self.first_name_on_account}   {self.second_name_on_account}   has  {self.all_accounts} accounts in the bank, and his balance is  {self.balance}")


    # def low_balance(self):
    #     if self.balance <= 0:
    #         print("add money")


    # def change_balance(self,x):
    #     self.balance += x
    #
    # def get_balance (self):
    #     return self.balance
    #
    # def print_all_accounts(self):
    #     print("total accounts opened -  ", *self.all_accounts)
    #
    #
    # def print_info (self):
    #     print ( f"first name  - {self.first_name_on_account} ")
    #     print ( f"second name  - {self.second_name_on_account} ")
    #     print (f"your balance is - {self.balance }")
    #     #print (f"total accounts opened {self.all_accounts} ")
    #     self.print_all_accounts()
