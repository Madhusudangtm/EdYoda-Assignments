# Write a Python program to square the elements of a list using map() function.
# Sample List: [4, 5, 2, 9]
# Square the elements of the list:
# [16, 25, 4, 81]
# Must have list as the input - 15
# Must Use map() function to solve the problem - 15
# Must give the expected output - 10


x = list(map(int,input('Enter numbers with space only: ').split()))
square_using_map = list(map(lambda i:i**2,x))
print(square_using_map)

# Output
# Enter numbers with space only: 2 3 4 5 6 7 8 9
# [4, 9, 16, 25, 36, 49, 64, 81]