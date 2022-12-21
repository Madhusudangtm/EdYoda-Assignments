# Write a Python Program to print full pyramid using '*' symbol. The pattern should be as shown below:

# *

# * * *

# * * * * *

# * * * * * * *

# * * * * * * * * *

def FullPyramid(x):
    for i in range(x):
        for j in range((i*2)+1):
            print('*',end=" ")
        print("\n") 

x = int(input('Enter a num: '))
FullPyramid(x)         


# Anather task of FullPyramid
# def FullPyramid(x):
#     y = 0
#     for i in range(1,x+1):
#         for j in range(1,(x-i)+1):
#             print(end=" ")

#         while y!= (i*2)-1:
#             print("*",end="")
#             y+=1 
#         # print("\n")       
#         y = 0 
#         print()

# x = int(input('Enter a num: '))
# FullPyramid(x)     

# Output
# Enter a num: 5
#     *    
#    ***   
#   *****  
#  ******* 
# *********