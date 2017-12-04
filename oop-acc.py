"""
>>> a = Account('Jim')
>>> a.holder
'Jim'
>>> a.balance
0
>>> b = Account('Jack')
>>> b.balance
0
>>> a is a
True
>>> a is not b
True
>>> c = a
>>> c is a
True
>>> tom_account = Account('Tom')
>>> tom_account.deposit(100)
100
>>> getattr(tom_account, 'balance')
100
>>> hasattr(tom_account, 'deposit')
True
>>> john = Account('John')
>>> type(john)
<class 'oop-acc.Account'>
>>> john.balance
0
>>> john.holder
'John'
>>> john.deposit(30)
30
>>> john.withdraw(30)
0
>>> john.withdraw(30)
'Insufficient funds'
>>> getattr(john, 'balance')
0
>>> john.deposit(100)
100
>>> getattr(john, 'balance')
100
>>> john.balance
100
>>> hasattr(john, 'balance')
True
>>> hasattr(john, 'cs61a')
False
>>> type(Account.deposit)
<class 'function'>
>>> tom_account.balance = 0
>>> Account.deposit(tom_account, 1001)
1001
>>> tom_account.deposit(1000)
2001
>>> tom_account = Account('Tom')
>>> jim_account = Account('Jim')
>>> tom_account.interest
0.02
>>> jim_account.interest
0.02
>>> Account.interest = 0.04
>>> tom_account.interest
0.04
>>> jim_account.interest = 0.08
>>> jim_account.interest
0.08
>>> tom_account.interest
0.04
>>> Account.interest = 0.05
>>> jim_account.interest
0.08
#the instance variable takes priority so 0.08 is not used for jim
>>> tom_account.interest
0.05
>>> ch = CheckingAccount('Tom')
>>> ch.interest
0.01
>>> ch.deposit(20)
20
>>> ch.withdraw(5)
14
"""

class Account:
    """An account has a balance and a holder"""
    #Class attribute
    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    #self is a name that refers to an instance of the account class that is being deposited into
    #only changing the balance of a particular instance
    #amount doesn't need a self bc it's passed in as an argument

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance
