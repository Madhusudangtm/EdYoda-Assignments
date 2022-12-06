# Reverse string approch 1

x = input("Enter the word or line: ")
z = list(x)
a = len(z)
for i in range(a):
    print(z[(a-1)-i],end="")
    

#Output

# Enter the word or line: I am EdYoda Data Science student
# tneduts ecneicS ataD adoYdE ma I
