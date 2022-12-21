# Take a number as input from the user.
# Print the number in reversed order.
# For example, for input 567, output should be: 765

num = int(input('Enter number: '))
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))

# Output
# Enter number: 526
# Reversed Number: 625