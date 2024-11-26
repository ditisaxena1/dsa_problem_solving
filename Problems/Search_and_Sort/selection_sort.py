"""
In selection sort we need to either select max or min element and then start sorting, and swap the elements
"""
# selected minimum element
array = [2,6,9,3,1,7]
min = 0

for i in range(0, len(array)-1):
    min = i
    for j in range(i+1,len(array)):
        if array[j]<array[min]:
            min = j
    array[i], array[min] = array[min], array[i]
    print(array)


# selected maximum element
def selection_sort(array):
    max = 0
    for i in range(len(array)-1):
        max = i
        for j in range(i+1, len(array)):
            if array[j] > array[max]:
                max = j
        array[i], array[max] = array[max], array[i]
        print(array)


array = [9,1,8,3,7,4,5,2]
selection_sort(array)
