# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
# The code must be implemented using Function - 15
# The function must accept the string - 15
# Count of upper-case characters must be printed - 5
# Count of lower case characters must be printed - 5

def count_up_low_chr():
    string = input("Enter a word or line: ")
    count_up = 0
    count_low = 0
    special_chr = 0
    for i in string:
        if ord(i)>=65 and ord(i)<=90:
            count_up = count_up+1
        elif ord(i)>=97 and ord(i)<=122:
            count_low = count_low+1
        else:
            special_chr = special_chr+1

    print("Count of upper-case characters: ", count_up)
    print("Count of lower-case characters: ", count_low)
    print("Count of special characters: ", special_chr)

count_up_low_chr()


# Output
# Enter a word or line: Madhusudan Gautam
# Count of upper-case characters:  2
# Count of lower-case characters:  14
# Count of special characters:  1
