# Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.
# sample input: 10
# sample output: 35
# should use lambda function to solve the problem - 15
# should print the output - 15

x = int(input('Enter a num: '))
add25 = lambda x:x+25
print('Expected output is: ',add25(x))

# Output
# Enter a num: 25
# Expected output is:  50