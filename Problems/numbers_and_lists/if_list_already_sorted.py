""""
Verify if the array/list is already sorted. Try first brute force approach and then optimize it
"""


# Brute Force Approach
"""
Time complexity: O(N^2)
Space complexity: O(N) - as using a temp_list
"""
def if_list_already_sorted(lst: list):
    if len(lst) == 1:
        return True
    else:
        temp_list = lst.copy()
        for i in range(len(temp_list)):
            for j in range(len(temp_list)-1):
                if temp_list[j] > temp_list[j+1]:
                    temp_list[j], temp_list[j+1] = temp_list[j+1], temp_list[j]
    if temp_list == lst:
        return True
    else:
        return False

print(if_list_already_sorted([2]))

# Optimal Approach using a boolean variable or number of swaps counter
"""
Time complexity: O(N) - as the outer loop is terminated after swapping in inner loop
Space complexity: O(1) - as the swapping is in place

"""

def if_list_sorted(lst: list):
    if len(lst) == 1:
        return True
    else:
        swap = False
        for i in range(len(lst)):
            for j in range(len(lst)-1):
                if lst[j] > lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
                    swap = True
            if swap:
                break

    if not swap:
        return True
    else:
        return False


print(if_list_sorted([1,2,3]))

