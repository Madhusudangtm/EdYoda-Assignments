# Handling a Bank Account

class Account:
    def __init__(self,title=None,balance=0):
        self.title=title
        self.__balance=balance
        print("Account holder name is: ",self.title)
        print("Dear "+self.title+", Your account balance is: ",self.__balance,'₹')      
    def getBalance(self):
        return print("Dear "+self.title+", Your account balance is: ",self.__balance,'₹')
    def deposit(self,amount):
        self.__balance = self.__balance+amount
        print('Dear '+self.title+", After deposit your balance is ",self.__balance,'₹')
    def withdraw(self,amount):
        self.__balance = self.__balance-amount
        print('Dear '+self.title+", After withdraw your balance is ",self.__balance,'₹')

class SavingsAccount(Account):
    def __init__(self,title=None,balance=0,intrestRate=0):
        super().__init__(title,balance)
        self.intrestRate=intrestRate
        self.__balance=balance
        print("Your yearly intrest rate is: ",self.intrestRate,"%")
    def intrestAmount(self):
        intrestAmount = (self.intrestRate*self.__balance)/100
        print('Dear '+self.title+", Your Yearly intrest amount is ",intrestAmount,'₹') 

# x = Account('msg',5000)
y = SavingsAccount('Madhusudan',50000,5)
y.deposit(5000)
y.withdraw(10000)
y.getBalance()
y.intrestAmount()

# Output
# Account holder name is:  Madhusudan
# Dear Madhusudan, Your account balance is:  50000 ₹
# Your yearly intrest rate is:  5 %
# Dear Madhusudan, After deposit your balance is  55000 ₹
# Dear Madhusudan, After withdraw your balance is  45000 ₹
# Dear Madhusudan, Your account balance is:  45000 ₹
# Dear Madhusudan, Your Yearly intrest amount is  2500.0 ₹