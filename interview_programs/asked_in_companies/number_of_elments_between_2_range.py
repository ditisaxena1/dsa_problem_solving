"""
1. You are given an unsorted array of integers and two integers, r1 and r2, which represent the inclusive range.
Your task is to count the number of elements in the array that fall within this range, including the boundaries.

𝐄𝐱𝐚𝐦𝐩𝐥𝐞:
𝐈𝐧𝐩𝐮𝐭:
Array = [1, 3, 5, 2]
r1 = 1
r2 = 5
Output:
4
"""

def no_of_elements_in_range(array, r1, r2):
    count = 0
    for i in range(len(array)):
        if r1 <= array[i] <= r2:
            count += 1

    return count

print(no_of_elements_in_range([1, 3, 5, 2], 0,3))