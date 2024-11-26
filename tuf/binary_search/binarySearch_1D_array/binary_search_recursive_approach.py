"""
Binary search using recursion
Time Complexity: O(logN)
"""

def binarySearch(array, low, high, target):
    if low > high:
        return -1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            return binarySearch(array, low, mid - 1, target)
        else:
            return binarySearch(array, mid+1, high, target)

print(binarySearch([1,2,3,4,5,8,10,12], 0, 7, 18))
