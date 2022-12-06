#fibonacci series 0,1,1,2,3,5,8,13,21,34

a = 1
b = 1

print("Fibonacci Series:")
while a<55:
    print(a," ",end = "")
    i = a + b
    a = b
    b = i

#output 
# Fibonacci Series:
# 1  1  2  3  5  8  13  21  34  