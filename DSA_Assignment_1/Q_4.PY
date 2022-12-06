# Q4. Write a program to print the first non-repeated character from a string?

def non_repeat_chr(s):
    fnc = ""
    for i in s:
        if s.count(i) == 1:
            print("First non-repeating character is", i)
            break
        else:
            print("Either all characters are repeating or string is empty")
            break
        

z = input("Enter str: ")
non_repeat_chr(z)
