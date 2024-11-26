"""
Input: arr[] = {3, 1, 3}
Output: Missing = 2, Repeating = 3
Explanation: In the array, 2 is missing and 3 occurs twice

Input: arr[] = {4, 3, 6, 2, 1, 1}
Output: Missing = 5, Repeating = 1
"""

# Brute Force
def missing_repeating(lst):
    n = len(lst)
    missing_num = 0
    rep_num = 0

    temp = [0]*n

    for i in range(n):
        temp[lst[i]-1] += 1
        if temp[lst[i]-1] > 1:
            rep_num = lst[i]

    for i in range(n):
        if temp[i] == 0:
            missing_num = i+1

    return temp, missing_num, rep_num

print(missing_repeating([3,1,3]))

# With one for loop

def missing_repeating(lst):
    n = len(lst)
    temp = [0]*n
    missing_num = 0
    rep_num = 0
    for i in range(n):
        temp[lst[i]-1] += 1
        if temp[lst[i]-1]>1:
            rep_num = lst[i]
        if temp[i] == 0:
            missing_num = i + 1

    return temp, missing_num, rep_num

print(missing_repeating([4, 3, 6, 2, 1, 1]))

