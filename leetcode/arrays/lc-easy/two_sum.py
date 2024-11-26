"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""


# brute force approach
"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def two_sum(nums: list[int], target: int) -> list[int]:
    index = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            two_sum = nums[i] + nums[j]
            if two_sum == target:
                index.append(i)
                index.append(j)
                break


    return index

print(two_sum([3,2,4], 6))


# Another approach - not good for all TCs
"""
Time Complexity: roughly O(n^2)
Space Complexity: O(1)
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        difference = target - nums[i]
        if difference in nums:
            return [i, nums.index(difference)]


print(two_sum(nums = [2,7,11,15], target = 9))


# Better approach handling all TCs and this code works in LC

"""
TC: O(n^2)
SC: O(1)
"""
def twosum(lst, target):
    if len(lst)==0 or len(lst)==1:
        return -1
    elif len(lst)==2:
        if sum(lst)==target:
            return 0,1
        else:
            return -1
    for i in range(len(lst)):
        diff = target - lst[i]
        if diff in lst and (lst.index(diff) != i):
            return i,lst.index(diff)

print(twosum([1,2,3,0,3,8], 6))


# Better/best approach having Time complexity as O(n) and Space Complexity O(1)

def two_sum(lst, target):
    lookup = {}  # dictionary to store value and its index
    for i, num in enumerate(lst): # this step takes o(n) time
        diff = target - num
        if diff in lookup:  # this step takes o(n) time
            return lookup[diff], i
        lookup[num] = i
    return -1
print(two_sum([1,2,3], 6)) # handles cases like empty list, or list does not have a match
print(two_sum([0,5,3,3,1], 6))


