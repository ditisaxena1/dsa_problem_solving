"""

Problem Statement: Given an array of N integers. Every number in the array except one appears twice. Find the single number in the array.

Example 1:
Input Format:
 arr[] = {1,1,2,2,3,3,4,5,5,6,6}
Result:
 4
Explanation:
 Only the number 4 appears once in the array.

Example 2:
Input Format:
 arr[] = {1,1,3,5,5}
Result:
 3
Explanation:
 Only the number 3 appears once in the array.
"""

#Brute Force Approach - 1

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""


def find_single_element(nums):
    if len(nums) == 1:
        return nums[0]

    for i in range(0, len(nums)):
        if i == 0:
            if nums[i] != nums[i+1]:
                return nums[i]
        elif i == len(nums)-1:
            if nums[i] != nums[-2]:
                return nums[i]
        elif nums[i] != nums[i+1] and nums[i] != nums[i-1]:
            return nums[i]


print(find_single_element([1, 1, 3, 3, 5, 5, 8]))


# using XOR Approach

"""
Time Complexity: O(n)
"""
def find_single_element_using_XOR(nums):
    number = 0
    for n in nums:
        number = number ^ n

    return number


print(find_single_element_using_XOR([1,1,2,2,3,3,4,4,8,8,9]))






