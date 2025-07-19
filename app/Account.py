class Account:
    def __init__(self, balance, number):
        self._balance = 0
        self.number = number


    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        if (balance<0):
            print("The balance cannot be negative.")
        else:
            self._balance = balance

    def withdrawal(self, value):
        if (self._balance>=value):
            self._balance-=value
            print("Withdrawal made successfully")
        else:
            print("Insufficient balance")


    def deposit(self, value):
        self._balance+=value

    def statement(self):
        print("Balance: ", self._balance)