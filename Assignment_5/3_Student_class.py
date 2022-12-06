# Implement the Complete Student Class
class Student:
    __name= ''
    __rollnum = ''
    def setName(self,x):
        self.__name = x
    def getName(self):
        return self.__name
    def setRollNumber(self,y):
        self.__rollnum=y
    def getRollNumber(self):
        return self.__rollnum
s = Student()
s.setName("Madhusudan")
s.setRollNumber(25)
print(s.getName())
print(s.getRollNumber())


#Output
# Madhusudan
# 25