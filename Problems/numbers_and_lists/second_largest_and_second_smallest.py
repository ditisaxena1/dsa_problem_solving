"""
We need to find the second largest and second smallest number in an array.

There can be multiple scenarios:
1. The array is sorted in ascending/descending order
2. The array has just one element in the array
3. The array has same elements
4. The array is unsorted - we can sort the array in ascending and find the second largest or second smallest based on index - with no duplicates
5. The array is unsorted - we can sort the array in ascending and find the second largest or second smallest based on index - with duplicates

"""

"""
Time Complexity: O(nlogn)
Space Complexity: O(1)
"""
# Case 1 : Array does not have duplicate elements
# Brute Force Approach


def find_second_largest_number(lst: list):
    # if list has just on element
    if len(lst) == 1:
        return -1

    else:
        lst.sort()
        return lst[-2]


def find_second_smallest_number(lst: list):
    # if list has just on element
    if len(lst) == 1:
        return -1

    else:
        lst.sort()
        return lst[1]


print(find_second_largest_number([2,1,4,5,3]))
print(find_second_smallest_number([2,1,4,5,3]))

print("\n\n")


"""
Time Complexity: O(nlogn) + O(n)-roughly equal to O(n)
Space Complexity: O(1)
"""
# Case 2 : Array have duplicate elements
# Brute Force Approach


def second_largest_number(lst: list):
    # if list has just on element
    if len(lst) == 1:
        return -1

    else:
        lst.sort()
        second_largest = 0
        largest = lst[-1]
        for num in range(len(lst)-2, -1, -1):
            if lst[num] < largest:
                second_largest = lst[num]
                break
    return second_largest


def second_smallest_number(lst: list):
    # if list has just on element
    if len(lst) == 1:
        return -1

    else:
        lst.sort()
        smallest = lst[0]
        second_smallest = 0
        for num in range(len(lst)):
            if lst[num] > smallest:
                second_smallest = lst[num]
                break

    return second_smallest


print(second_largest_number([2,1,4,5,3]))
print(second_smallest_number([2,1,4,5,3]))


# Better approach

def second_largest(list):
    largest = 0
    second_largest = -1
    for i in list:
        if i > largest:
            second_largest = largest
            largest=i
        elif i >second_largest and i != largest:
            second_largest = i
    return largest, second_largest

def second_smallest(list):
    smallest = float("inf")
    second_smallest = float("-inf")

    for num in list:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest, smallest


print(second_largest([6,1,3,4,10,11,11,11,12]))
print(second_smallest([6,-1,3,-4,10,11,11,11,12]))






