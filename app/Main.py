class Main:
    pass

from Client import Client

from Account import Account

c1=Client("João", "8199233-5678")

account=Account(c1.get_name(), 164521)

account.deposit(100)
account.withdrawal(50)
account.statement()
