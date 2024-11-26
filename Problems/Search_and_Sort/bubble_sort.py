def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
        print(array, end="\n\n")

    print("final sorted array", array)


array = [10,5,7,4,2,8,9,21,17,1,0,6,15]
bubble_sort(array)


"""
OPTIMIZED SOLUTION - for checking if array is already sorted in ascending order

"""


def is_sorted_in_ascending_order(array):
    swap = False
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                swap = True
                array[j], array[j+1] = array[j+1], array[j]

        print(array)
        if swap is False:
            print("already sorted in ascending")
            break


print(is_sorted_in_ascending_order([1,2,3,4,5]))


