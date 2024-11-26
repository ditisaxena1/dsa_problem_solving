def scnd_and_thrd_largest(array):
    length = len(array)
    if length < 3:
        return None
    elif length >= 3:
        temp =0
        array = list(set(array))
        for i in range(length):
            for j in range(length-1):
                if array[j] < array[j+1]:
                    temp = array[j+1]
                    array[j+1] = array[j]
                    array[j] = temp

        return array[1], array[2]

array = [10,20,30]
print(scnd_and_thrd_largest(array))

