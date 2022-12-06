# Q3. Write a program to check if two strings are a rotation of each other?

def checkRotation(s1, s2): 
    temp = ''  
    if len(s1) != len(s2): 
        return False 
    temp = s1 + s2 

    if s2 in temp: 
        return True 
    else: 
        return False
 
string1 = "MADHU SUDAN"
string2 = "NADUS UHDAM"
  
if checkRotation(string1, string2): 
    print("Given Strings are rotations of each other.")
else: 
    print("Given Strings are not rotations of each other.")