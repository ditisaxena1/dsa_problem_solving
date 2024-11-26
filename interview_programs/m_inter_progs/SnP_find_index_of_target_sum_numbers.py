"""
if I have a target sum = 7
and the list is [1,3,4,2,6]

then the numbers that add upto 7 is 3 and 4
return the index of 3 and 4 that is 1,2


"""

def find_index_of_numbers(nums, target):
    for i in range(len(nums)):
        difference = target - nums[i]
        if difference in nums:
            print(i, nums.index(difference))
            break

print(find_index_of_numbers([1,3,4,2,6], 7))