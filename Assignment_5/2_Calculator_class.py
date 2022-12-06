# Implement a Calculator Class

class Calculator:

    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        print("Addition is: ",self.num1+self.num2)
    def subtract(self):
        print("Substraction is: ",self.num2-self.num1)
    def multiply(self):
        print("Multiplication is: ",self.num1*self.num2)
    def divide(self):
        print("Divide is: ",self.num2/self.num1)

x=Calculator(10,20)
x.add()
x.subtract()
x.multiply()
x.divide()

# Output
# Addition is:  30
# Substraction is:  10
# Multiplication is:  200
# Divide is:  2.0