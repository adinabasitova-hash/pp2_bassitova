class Account:
  def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance

  def deposit(self):
    print('How much money would you like to put?')
    x = int(input())
    self.balance += x
  def withdraw(self):
    print('How much money would you like to get?')
    y = int(input())
    if self.balance >= y:
      self.balance -= y
    else:
      print('Not enough money')

acc = Account('Adina', 1000)
acc.deposit()
acc.withdraw()

print(acc.balance)  