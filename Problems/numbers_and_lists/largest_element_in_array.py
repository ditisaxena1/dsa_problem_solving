"""
Find the largest element in an array of integers

"""

def largest(array):

    largest = 0

    for i in range(len(array)):
        if array[i] > largest:
            largest = array[i]


    return largest


print(largest([1, 2,3,4,5]))

"""
find largest and second largest element in an array
"""

def largest_secondlargest(list):
    largest = 0
    second_largest = -1
    for i in list:
        if i > largest:
            second_largest = largest
            largest=i
        elif i >second_largest and i != largest:
            second_largest = i
    return largest, second_largest

print(largest_secondlargest([6,1,3,0,9,11,11,12]))