"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
Input: nums = [4,1,2,1,2]
Output: 4

"""

from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        nums_dict = Counter(nums)
        for i,j in nums_dict.items():
            if j == 1:
                return i

ob = Solution()
nums = [2,2,1,3,1]
print(ob.singleNumber(nums))