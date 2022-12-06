# Even odd Problem approch 1

s = {11,8,32,55,71,17,56,89,54,16,19,67}
even = 0
odd = 0
for i in s:
    if i%2==0:
        even = even+1
    else:
        odd = odd+1    
print("Number of even numbers: ",even)
print("Number of odd numbers: ",odd)

# Output
# Number of even numbers:  5
# Number of odd numbers:  7

