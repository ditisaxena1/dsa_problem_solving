"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

"""

def find_occurence(array, num):    #[2,4,6,8,8,9,10,8]
    start_index = -1
    end_index = -1
    count = 0
    for i in range(0, len(array)):
        if array[i] == num:
            if count == 0:
                start_index = i
                count += 1
            else:
                end_index = i

    return start_index, end_index

print(find_occurence([], 1))

print(find_occurence([5,7,7,8,8,8,8,10], 8))


#  Using Optimal method - Binary Search

"""
Time Complexity: O(logN)
"""
def first_occurence(array, num):
    start_index = -1
    low, high = 0, len(array) - 1

    while low <= high:
        mid = (low+high)//2

        if array[mid] == num:
            start_index = mid
            high = mid - 1
        elif array[mid] > num:
            high = mid - 1
        else:
            low = mid+1

    return start_index


def last_occurence(array, num):
    last_index = -1
    low, high = 0, len(array) - 1

    while low <= high:
        mid = (low+high)//2

        if array[mid] == num:
            last_index = mid
            low = mid + 1
        elif array[mid] > num:
            high = mid - 1
        else:
            low = mid+1

    return last_index


def first_and_last_occurence(array, num):
    f = first_occurence(array, num)
    l = last_occurence(array, num)
    return f,l

print(first_and_last_occurence([5,7,7,8,8,8,8,8,9,10], 8))