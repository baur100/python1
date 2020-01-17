class Bank:

    def __init__(self, first_name_on_account, second_name_on_account, balance, all_accounts):
        self._first_name_on_account = first_name_on_account
        self._second_name_on_account = second_name_on_account
        self._balance = balance
        self._all_accounts = all_accounts

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, i):
        if i < 0:
            print("add money   ")
        if i > 1000000:
            raise ValueError("too much")
        self._balance = i

    @property
    def all_accounts(self):
        return self._all_accounts

    @all_accounts.setter
    def all_accounts(self,value):
        self._all_accounts=value

    @property
    def first_name_on_account(self):
        return self._first_name_on_account

    @first_name_on_account.setter
    def first_name_on_account(self,j):
        self._first_name_on_account = j

    def __repr__(self):
        return (
            f"{self._first_name_on_account}   {self._second_name_on_account}   has  {self._all_accounts} accounts in the bank, and his balance is  {self.balance}")
