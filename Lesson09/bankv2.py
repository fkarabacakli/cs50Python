class Bank():
    def __init__(self):
        self.balance = 0

    def __str__(self):
        return f"{self.balance}"
        
    def deposit(self,n):
        self.balance += n

    def withdraw(self,n):
        self.balance -= n

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self,balance):
        if balance<0:
            raise ValueError("Balance can not be less than zero!!!")
        self._balance = balance
    

bank = Bank()
bank.deposit(100)
bank.withdraw(10)
bank.deposit(50)
bank.deposit(20)
bank.withdraw(50)
print(f"Balance: {bank}")

