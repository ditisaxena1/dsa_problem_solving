"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""

def move_zeroes(nums):
    index = 0
    if len(nums) == 1:
        return nums
    else:
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1
        for i in range(index, len(nums)):
            nums[i] = 0

    return nums

print(move_zeroes([0]))




def move_zeroes(num:list[int]):
    non_zero_index = 0
    for n in range(0, len(num)):
        if num[n] != 0:
            num[non_zero_index], num[n] = num[n], num[non_zero_index]
            non_zero_index += 1

    print(num)

num = [0,3,5,1,2,8,0,7]
move_zeroes(num)

