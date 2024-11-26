"""
given an aray sort it based on the frequency of the array. if two element have same frequency then sort
them based on the ascending order
I/P - [ 1,2,6,2,6,2,2]
O/P - [ 1,6,6,2,2,2,2]


"""
from collections import Counter


def sort_array_based_on_frequency(array):
    frequencies = Counter(array)
    value_sorted_array = sorted(frequencies.items(), key=lambda x: x[1])
    for key, value in value_sorted_array:
        for i in range(value):
            print(key, end=" ")

sort_array_based_on_frequency([1,2,3,3,4,4,1,6,6,6,5,5,5])
