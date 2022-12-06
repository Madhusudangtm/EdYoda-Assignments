# Implement a Banking Account

class Account:
    def __init__(self,title=None,balance=0):
        self.title=title
        self.balance=balance
        print("Account holder name is: ",self.title)
        print("Dear "+self.title+", Your account balance is: ",self.balance,'₹')      

class SavingsAccount(Account):
    def __init__(self,title=None,balance=0,intrestRate=0):
        super().__init__(title,balance)
        self.intrestRate=intrestRate
        print("Your intrest rate is: ",self.intrestRate,"%")

x = Account("Msg",2000000)
y = SavingsAccount('Madhusudan',50000,5)

# Output
# Account holder name is:  Msg
# Dear Msg, Your account balance is:  2000000 ₹
# Account holder name is:  Madhusudan
# Dear Madhusudan, Your account balance is:  50000 ₹
# Your intrest rate is:  5 %