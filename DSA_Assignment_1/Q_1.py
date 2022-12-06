# Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

def sum_pair(s,l):
    y = len(s)
    for i in range(y):
        for j in range(i+1,y):
            if (s[i]+s[j]) == l:
                print('(',s[i],',',s[j],')')
l = 4
z = [1,5,3,6,8,4,1,2,3,1,2]
sum_pair(z,l)
