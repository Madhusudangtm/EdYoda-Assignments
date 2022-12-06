# Write a Python program to triple all numbers of a given list of integers. Use Python map.
# sample list: [1, 2, 3, 4, 5, 6, 7]
# Triple of list numbers:
# [3, 6, 9, 12, 15, 18, 21]
# Must use map to find the expected output - 30

x = list(map(int,input('Enter numbers with space only: ').split()))
Triple_With_Map = list(map(lambda i:i*3,x))
print(Triple_With_Map)


# Output
# Enter numbers with space only: 10 2 66 30 5 30 3
# [30, 6, 198, 90, 15, 90, 9]