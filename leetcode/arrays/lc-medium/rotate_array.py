"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

"""
# Anticlockwise rotation
def rotate_array(nums:list[int], d: int):
    n = len(nums)
    # Ensure d is within the bounds of the array length
    d = d % n

    temp_arr = []

    # First, add elements from index d to the end of the array
    for i in range(d, n):
        temp_arr.append(nums[i])

    # Then, add elements from the start of the array to index d-1
    for i in range(0, d):
        temp_arr.append(nums[i])

    return temp_arr


print(rotate_array([1,2,3,4,5,6,7], 2))


# Clockwise rotation
def rotate_array(nums, k):
    n = len(nums)

    k = k % n

    temp_arr = []

    for i in range(n-k, n):
        temp_arr.append(nums[i])

    for i in range(n-k):
        temp_arr.append(nums[i])

    return temp_arr


print(rotate_array([1,2,3,4,5,6,7], 2))


def rotate_array_using_slicing(nums:list[int], d: int) -> list[int]:
    n=len(nums)
    d = d % n
    return nums[d:] + nums[0:d]


print(rotate_array_using_slicing([-1,-100,3,99], 2))

# short optimised code

def right_rotate(lst: list, d) -> list:
    n = len(lst)
    d = d % n

    return lst[n - d:n] + lst[:n - d]


print(right_rotate([1, 2, 3, 4, 5, 6, 7, 8], 3))


# [4,5,6,7,1,2,3]

def left_rotate(lst: list, d) -> list:
    n = len(lst)
    d = d % n

    return lst[d:n] + lst[:d]


print(left_rotate([1, 2, 3, 4, 5, 6, 7], 3))



