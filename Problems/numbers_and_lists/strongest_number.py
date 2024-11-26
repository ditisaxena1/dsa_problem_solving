"""
Given an array arr[] of N positive integers. The task is to find the maximum for every adjacent pair in the array.

Examples:

Input: 1 2 2 3 4 5
Output: 2 2 3 4 5

Input: 5 5
Output: 5
"""

def strongest_number(arr):
    index = 0
    while index < len(arr) - 1:
        if arr[index] >= arr[index + 1]:
            print(arr[index])
        else:
            print(arr[index+1])

        index += 1

strongest_number([5,5])

