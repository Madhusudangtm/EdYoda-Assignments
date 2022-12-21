# Write a Python Program to print half pyramid using alphabets. The pattern should be as shown below:

# A

# B B

# C C C

# D D D D

# E E E E E

def HalfPyramid(l1):
    for i in range(len(l1)):
        for j in range(i+1):
            print(l1[i],end=" ")
        print("\n") 

x = ['A','B','C','D','E']
HalfPyramid(x)           
