"""
Input: arr[] = {10, 5, 3, 4, 3, 5, 6, 10}
Output: 10
Explanation: 10 is the first element that repeats
"""


def repeating(lst):
    for i in range(len(lst)):
        for j in range(i, len(lst)-1):
            if lst[i] == lst[j+1]:
                return lst[i]
    return -1


print(repeating([10, 5, 3, 4, 3, 5, 6, 10]))