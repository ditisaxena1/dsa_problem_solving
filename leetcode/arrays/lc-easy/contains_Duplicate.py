"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

from collections import Counter


def sup(lst):
    # if len(lst) == 1:
    #     return False
    # freq = [0] * max(lst)
    # for i in range(len(lst)):
    #     freq[lst[i]-1] += 1
    #     if freq[lst[i]-1]>1:
    #         return True

    freq = Counter(lst)
    print(freq)
    for i in freq.values():
        if i > 1:
            return True
    return False

print(sup([3,-3]))