# 1. Create a class named ‘Dog’.
# It should have a constructor which accepts its name, age and coat color.
# You must perform the following operations:
# a. It should have a function ‘description()’ which prints the name and age of the dog.
# b. It should have a function ‘get_info()’ which prints the coat color of the dog.
# c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’.
# It should have at least two methods of its own.
# d. Create objects and implement the above functionalities.

class Dog:
    def __init__(self,name,age,coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    def description(self):
        print('Dog name is: ',self.name)
        print('Age of ',self.name,' is: ', self.age)    
    def get_info(self):
        print('Coat color of ',self.name,' is: ',self.coat_color)

class JackRussellTerrier(Dog):
    def health(self):
        print('The breed has a reputation for being healthy.')
        print('Jack Russells can live from 13 to 16 years.')
    def Crossbreeds(self):
        print('Crossbreed of a Jack Russell terrier and a Beagle is called a Jackabee.')    
class Bulldog(Dog):
    def health(self):
        print('The average life span of the breed as 8 to 10 years.')
        print('Allergies and hip issues in older Bulldogs')
    def Appearance(self):
        print('Thick folds of skin on the brow, round, black, wide set eyes.')
        print('A rope or nose roll above the nose.')

dog = Bulldog('Jaky',5,'Black')
dog.description()
dog.get_info()        
dog.health()
dog.Appearance()

dog1 = JackRussellTerrier('Harry',4,'Brown')
dog1.description()
dog1.get_info()
dog1.health()
dog1.Crossbreeds()

# Output
# Dog name is:  Jaky
# Age of  Jaky  is:  5
# Coat color of  Jaky  is:  Black
# The average life span of the breed as 8 to 10 years.
# Allergies and hip issues in older Bulldogs
# Thick folds of skin on the brow, round, black, wide set eyes.
# A rope or nose roll above the nose.
# Dog name is:  Harry
# Age of  Harry  is:  4
# Coat color of  Harry  is:  Brown
# The breed has a reputation for being healthy.
# Jack Russells can live from 13 to 16 years.
# Crossbreed of a Jack Russell terrier and a Beagle is called a Jackabee.