def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: already sorted

    pivot = arr[len(arr) // 2]  # Choose the pivot as the middle element
    left = [x for x in arr if x < pivot]  # Elements smaller than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot

    return quick_sort(left) + middle + quick_sort(right)

# Example Usage:
my_list = [0,0,1,2,1,2]
sorted_list = quick_sort(my_list)
print("Sorted array:", sorted_list)