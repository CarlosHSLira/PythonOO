class Main:
    pass

print("Testando projeto")

from Client import Client

from Account import Account

# a declaração de um novo objeto se dá
# semelhantemente a declaração de uma variável
c1=Client("João", "8199233-5678")

account = Account(c1.name, 164521, 0)

print("Holder: ", account.holder, "| Number: ", account.number, "| Balance: ",account.balance)