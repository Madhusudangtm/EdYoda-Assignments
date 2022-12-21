# Given an array of integers, find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order. 
# Examples:  
# Input: arr[] = {1, 9, 3, 10, 4, 20, 2}
# Output: 4
# Explanation: The subsequence 1, 3, 4, 2 is the longest subsequence of consecutive elements
# Input: arr[] = {36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42}
# Output: 5
# Explanation: The subsequence 36, 35, 33, 34, 32 is the longest subsequence of consecutive elements.



def findLongestConseqSubseq(arr, n):
 
    ans = 0
    count = 0
 
    # Sort the array
    arr.sort()
 
    v = []
 
    v.append(arr[0])
 
    # Insert repeated elements only
    # once in the vector
    for i in range(1, n):
        if (arr[i] != arr[i - 1]):
            v.append(arr[i])
 
    # Find the maximum length
    # by traversing the array
    for i in range(len(v)):
 
        # Check if the current element is
        # equal to previous element +1
        if (i > 0 and v[i] == v[i - 1] + 1):
            count += 1
 
        # Reset the count
        else:
            count = 1
 
        # Update the maximum
        ans = max(ans, count)
 
    return ans
 
 
# Driver code
arr = [1,9,3,10,4,20,2]
n = len(arr)
 
print("Length of the Longest contiguous subsequence is",
      findLongestConseqSubseq(arr, n))