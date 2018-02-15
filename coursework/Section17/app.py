from Account import Checking

account = Checking("data/balance.txt", 1.00)
account.withdraw(30)
print(account.balance)
account.deposit(30)
print(account.balance)
