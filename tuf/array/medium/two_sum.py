# using dictionary approach for displaying index of the numbers which sum to the target value

def two_sum(nums, target):
    hash = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hash:
            return [hash[diff], i]
        else:
            hash[num] = i

    return -1

print(two_sum([2,2], 4))

