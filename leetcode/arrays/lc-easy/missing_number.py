""""
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the
range since it does not appear in nums.



"""


class Solution(object):
    def missingNumber(self, nums):
        i = 0
        while i < (len(nums) + 1):
            if i not in nums:
                return i
            i += 1
    #     for i in range(0, len(nums)+1):
    #         if i not in nums:
    #             return i


ob = Solution()
nums=[0,2,3]
print(ob.missingNumber(nums))

# Second way - using direct method of sum calculation for first n numbers

def missingNumber(nums):
    size = len(nums)
    expected_sum = (size*(size+1))//2
    actual_sum = sum(nums)

    return expected_sum - actual_sum
print(missingNumber([9,6,4,2,3,5,7,0,1]))





