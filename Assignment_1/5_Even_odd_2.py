# Even odd approach 2

x = [5,99,8,85,24,36,47,38,49,77]
y = 0
even = 0
odd = 0
while y<len(x):
    if x[y]%2 == 0:
        even = even+1
    else:
      odd = odd+1    
    y = y+1
print("Number of even numbers is: ",even)
print("Number of odd numbers is: ",odd)

# Output
# Number of even numbers is:  4
# Number of odd numbers is:  6