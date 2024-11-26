"""
Question: Given an unsorted array of integers, find the kth largest element in the array.
The kth largest element is the element that would be in the kth position if the array were sorted in descending order.
Example:
Input:
arr = [3, 2, 1, 5, 6, 4]
k = 2
Output:
5
Explanation:
If the array is sorted in descending order, it becomes [6, 5, 4, 3, 2, 1]. The 2nd largest element is 5.

"""

def find_kth_largest_element(arr, k):
    if len(arr) <= k:
        return -1
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if i == k-1:
            return arr[-k]



print(find_kth_largest_element([3, 2, 1, 5, 6, 4], 2))

