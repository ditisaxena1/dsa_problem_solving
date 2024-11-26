"""
Question: Given an array of integers, find the largest number that does not have any duplicates in the array.
Example:
Input:
arr = [4, 3, 2, 7, 3, 4, 8]
Output:
8
Explanation:
The unique numbers are [2, 7, 8], and the largest among them is 8.

"""

# Using Mapping
from collections import Counter


def find_largest_num(arr):
    map = Counter(arr)
    maxi = -1
    for k,v in map.items():
        if v == 1:
            maxi = max(maxi, k)

    return maxi


print(find_largest_num([4, 3, 2, 7, 3, 4, 8]))

print("\n\n")


