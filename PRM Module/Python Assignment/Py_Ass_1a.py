# Python Candidates - Question 1
# You will have a number of elements and in the next n lines element of a list. You have to create a list from the given strings. You have to sort the list based on 2nd last character of a string.
# For example: given list = ['great','hello','hiyo','abc'] so your output_dictionary should be ['great', 'abc', 'hello','hiyo']
# Input Format:
# At first-line it will have an integer (number of elements inside a list). In the second line, it will have a string.
# Output Format:
# A single line containing a sorted list.

# Method 1
n = int(input())
m = [input() for i in range(n)]
m.sort(key=lambda x:x[-2])
print(m)

# input
# 2
# mdc
# mad

# output
# ['mad', 'mdc']
