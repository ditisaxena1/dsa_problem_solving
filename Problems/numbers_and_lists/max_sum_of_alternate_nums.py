"""
Find max sum of alternate numbers such that if list is [1,2,1,4,5,6] then max sum will be a sum of numbers at index 1,3,5
and the numbers are 2,4,6 and total is 12

I/P -- [1,2,1,4,5,6]
O/P - 12
"""


def max_sum_of_alternate_numbers(lst:list):
    if len(lst) == 0:
        return -1
    elif len(lst) == 1:
        return lst
    max_sum = 0
    for i in range(len(lst)):
        index = i
        sum = 0
        while index < len(lst):
            sum += lst[index]
            index += 2
        max_sum = max(max_sum, sum)

    return max_sum


# print(max_sum_of_alternate_numbers([1,2,1,4,5,6,9,10]))
# print(max_sum_of_alternate_numbers([]))
# print(max_sum_of_alternate_numbers([1]))
# print(max_sum_of_alternate_numbers([1,2]))


def max_consecutive_sum(lst):
    if len(lst) == 0:
        return -1
    elif len(lst) == 1:
        return lst
    max_sum = 0
    for i in range(len(lst)-2):
        sum = 0
        j = i
        while j < i+3:
            sum += lst[j]
            j += 1
        max_sum = max(max_sum, sum)
    return max_sum


print(max_consecutive_sum([1,2,3,4,5]))