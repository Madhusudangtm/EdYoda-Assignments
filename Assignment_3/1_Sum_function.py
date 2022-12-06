# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20
# Explanation:
# Summation should like 8+2+3+0+7 = 20
# Should have used function to implement the code - 15
# Must print the Expected output - 15

list = [2,10,52,46,13,9,87]
def sum_list():
    sum = 0
    for i in list:
        sum += i
    print("Sum of all numbers in list is:",sum)

sum_list()

# Output
# Sum of all numbers in list is: 219