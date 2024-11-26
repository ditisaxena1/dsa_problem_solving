"""
Given an array consisting of only 0s, 1s, and 2s. Write a program to in-place sort the array without using inbuilt sort functions. ( Expected: Single pass-O(N) and constant space)

Examples
Input:
 nums = [2,0,2,1,1,0]
Output
: [0,0,1,1,2,2]

Input:
 nums = [2,0,1]
Output:
 [0,1,2]

Input:
 nums = [0]
Output:
 [0]

"""
# Better Approach
"""
Time Complexity: O(N) + O(N) which is O(N)
Space Complexity: O(1)
"""
def sort_numbers(nums):
    count_0 , count_1, count_2 = 0,0,0

    for num in nums:
        if num == 0:
            count_0 += 1
        elif num == 1:
            count_1 += 1
        elif num == 2:
            count_2 += 1

    for i in range(0, count_0):
        nums[i] = 0
    for j in range(count_0, count_1+count_0):
        nums[j] = 1
    for k in range(count_1+count_0, len(nums)):
        nums[k] = 2

    return nums

print(sort_numbers([2,0,2,1,1,0]))


# Optimal Approach using Dutch National Flag of Algorithm - we will use three [pointers here low, mid and high

def sort_numbers_0_1_2(nums):
    low, mid = 0,0
    high = len(nums)-1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid],nums[low]
            mid += 1
            low += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[high], nums[mid] = nums[mid],nums[high]
            high -= 1

    return nums

print(sort_numbers_0_1_2([1,0,0,2,1,2,1,0,0]))





