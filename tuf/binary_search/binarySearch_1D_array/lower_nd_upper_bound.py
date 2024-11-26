"""

find lower bound index such that if I have an sorted array [1,2,4,6,8,10,12,14,16,18] and I want the lower index at which array[index] >= target value
"""
"""
Time Complexity: O(LogN) for both the problems
"""
def lower_bound(array, target):
    low_index = len(array)
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] >= target:
            low_index = mid
            high = mid - 1
        else:
            low = mid+1

    return low_index

print(lower_bound([1,2,4,6,8,10,12,14,16,18,18], 18))


"""

find upper bound index such that if I have an sorted array [1,2,4,6,8,10,12,14,16,18] and I want the lower index at which array[index] >target value
"""

def upper_bound(array, target):
    up_index = 0 # let us suppose
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] > target:
            up_index = mid
            high = mid - 1
        else:
            low = mid+1

    return up_index

print(upper_bound([1,2,4,6,8,10,12,18], 8))

"""
You are given a sorted array arr of distinct values and a target value x. You need to search for the index of the target value in the array.

If the value is present in the array, then return its index. Otherwise, determine the index where it would be inserted in the array while maintaining the sorted order.

"""

def searchInsertIndex(array, target):
    index = len(array)
    low,high = 0, len(array)-1

    while low <= high:
        mid = (low+high)//2
        if array[mid] >= target:
            index = mid
            high = mid-1
        else:
            low = mid+1

    return index

print(searchInsertIndex([1,2,4,7], 6))


