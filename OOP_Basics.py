class Student():
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    def study(self):
        print(f"{self.name} got Grade {self.grade}.")
        print(f"{self.name} is learning")
S1=Student("ram","A")
S2=Student("Lenin","B")
S1.study()
S2.study()

#Bank account 

class Bank_account:
    def __init__(self,Name,Balance):
        self.name=Name
        self.balance=Balance
    def deposit(self,amount):
        self.balance+=amount
        print(F"Balance of {self.name} is {self.balance}")
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"{amount} is debited")
            print(f"current_balance of {self.name} is {self.balance}")
        else:
            print("Insufficient balance")
            print(f"Current balance of {self.name} is {self.balance}")
    def show_balance(self):
        print(f"Balance amount:{self.balance}")

A1=Bank_account("Thomas",10000)
A2=Bank_account("Henry",25000)

A1.deposit(2500)
A1.withdraw(13000)
A1.show_balance()

A2.deposit(12000)
A2.withdraw(1200)
A2.show_balance()
A2.withdraw(250)