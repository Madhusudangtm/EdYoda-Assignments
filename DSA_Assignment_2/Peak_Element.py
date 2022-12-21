# Given an array arr[] of integers. Find a peak element i.e. an element that is not smaller than its neighbors. 
# Note: For corner elements, we need to consider only one neighbor. 
# Example:
# Input: array[]= {5, 10, 20, 15}
# Output: 20
# Explanation: The element 20 has neighbors 10 and 15, both of them are less than 20.
# Input: array[] = {10, 20, 15, 2, 23, 90, 67}
# Output: 20 or 90
# Explanation: The element 20 has neighbors 10 and 15, both of them are less than 20, similarly 90 has neighbors 23 and 67.


def findPeak(nums, left=None, right=None):
 
    # Initialize left and right
    if left is None and right is None:
        left, right = 0, len(nums) - 1
 
    # find the middle element. To avoid overflow, use mid = left + (right - left) / 2
    mid = (left + right) // 2
 
    # check if the middle element is greater than its neighbors
    if ((mid == 0 or nums[mid - 1] <= nums[mid]) and
            (mid == len(nums) - 1 or nums[mid + 1] <= nums[mid])):
        return mid
 
    # If the left neighbor of `mid` is greater than the middle element,
    # find the peak recursively in the left sublist
    if mid - 1 >= 0 and nums[mid - 1] > nums[mid]:
        return findPeak(nums, left, mid - 1)
 
    # If the right neighbor of `mid` is greater than the middle element,
    # find the peak recursively in the right sublist
    return findPeak(nums, mid + 1, right)
 
 
def findPeakElement(nums) -> int:
 
    # base case
    if not nums:
        exit(-1)
 
    index = findPeak(nums)
    return nums[index]
 
 
if __name__ == '__main__':
 
    nums = [5,10,20,15]
    print('The peak element is', findPeakElement(nums))