def uncommon_element(array1, array2):

    new_array = []
    """
    the length comparison is not required for the uncommon elements but for common elements.
    """
    # if len(array1) < len(array2):
    #     big_array, small_array = array2, array1
    # else :
    #     big_array, small_array = array1, array2
    set1 = set(array1)
    set2 = set(array2)

    for i in set1:
        if i not in set2:
            new_array.append(i)
        else:
            continue
    for i in set2:
        if i not in set1:
            new_array.append(i)
        else:
            continue

    return new_array


array1 = [1,2,1,2,4,5,4]
array2 = [6,7,6,8,5,2]

print(uncommon_element(array1, array2))

