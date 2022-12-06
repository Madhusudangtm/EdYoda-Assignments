# Square Numbers and Return Their Sum

class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        self.x = self.x**2
        self.y = self.y**2
        self.z = self.z**2
        sum = self.x + self.y + self.z
        print('Your expected output is:',sum)
x=Point(1,3,5)
x.sqSum()

# Output
# Your expected output is: 35