"""
find the element which is greater than or equal to x in an array
find the element which is smaller than or equal to x in an array

"""


def floor_and_ceil(array, target):
    low = 0
    high = len(array) - 1
    floor, ceil = -1, -1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] >= target:
            ceil = array[mid]
            high = mid - 1
        else:
            low = mid + 1
        if array[mid] <= target:
            floor = array[mid]
            low = mid + 1
        else:
            high = mid - 1

    return ceil, floor


print(floor_and_ceil([1,3,5,7,10,13,17,19,21], 18))










