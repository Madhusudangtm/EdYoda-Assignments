# Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"
# Should have used the function in the code - 15
# Must get the expected output - 15

def reverse_string():
    x = input("Enter the string: ")
    y = ''
    for i in x:
        y = i + y
    print(y)

reverse_string()

# Output
# Enter the string: 1234abcd
# dcba4321