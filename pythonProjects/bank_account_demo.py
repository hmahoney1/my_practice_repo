from bank_account import BankAccount

account1 = BankAccount("1234", 1000)
print(account1) # this calls the string method defined in the class
account1.deposit(1000)
print(account1)
account1.withdraw(54)
print(account1)

account2 = BankAccount("Harrys Account", 50000)
print(account2)
account2.withdraw(60000)
print(account2)