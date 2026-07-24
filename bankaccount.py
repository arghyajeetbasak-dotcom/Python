class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        print(f"Account holder's name: {self.name}")
        print(f"Balance: {self.balance}")
    def deposit(self,amount):
        print(f"Rs.{amount} deposited succesfully")
        self.balance=self.balance+amount
    def withdraw(self,amount):
        if(self.balance-amount<1000):
            print("Money canot be withdrawn")
            return
        print(f"Rs.{amount} withdrawn succesfully")
        self.balance=self.balance-amount
    def display_balance(self):
        print(f"Account balance is {self.balance}")
obj=BankAccount("Arghyajeet Basak",1500)
obj.deposit(0)
obj.withdraw(900)
obj.display_balance()