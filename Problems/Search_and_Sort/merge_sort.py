"""
Follows Divide and  Conquer approach. Recursion is used here.
Array is continuously divided into left and right part until individual elements are separated

"""


def merge_sort(array, low, high):
    if low == high:
        return
    mid = (low + high) // 2
    merge_sort(array, low, mid)
    merge_sort(array, mid + 1, high)

    merge(array, low, mid, high)

def merge(array, low, mid, high):

    left_array = array[low:mid+1]
    right_array = array[mid+1:high+1]

    left_index = 0
    right_index = 0
    sorted_index = low

    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] <= right_array[right_index]:
            array[sorted_index] = left_array[left_index]
            left_index += 1
        else:
            array[sorted_index] = right_array[right_index]
            right_index += 1
        sorted_index += 1

    while left_index < len(left_array):
        array[sorted_index] = left_array[left_index]
        left_index += 1
        sorted_index += 1

    while right_index < len(right_array):
        array[sorted_index] = right_array[right_index]
        right_index += 1
        sorted_index += 1

list1 = [1,2,5,4,3]
low = 0
high = len(list1)-1

merge_sort(list1, low, high)
print(list1)