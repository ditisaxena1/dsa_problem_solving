"""
Our task is to print the element which occurs 3 consecutive times in a Python list.
Example :

Input : [4, 5, 5, 5, 3, 8]

Output : 5

Input : [1, 1, 1, 64, 23, 64, 22, 22, 22]

Output : 1, 22

"""

def num_occuring_3_consecutive_times(lst):
    count = 1
    index = 0
    new_list = []

    while index < len(lst)-1:
        if lst[index] == lst[index+1]:
            count += 1
            index += 1

        else:
            if count >= 3:
                new_list.append(lst[index])
            count = 1
            index = index + 1

    if count >= 3:
        new_list.append(lst[index])

    return new_list

print(num_occuring_3_consecutive_times([1, 1, 1, 64, 23, 64, 22, 22, 22]))


"""
gfg short solution
"""

# creating the array
arr = [4, 5, 5, 5, 3, 8]

# size of the list
size = len(arr)

# looping till length - 2
for i in range(size - 2):

    # checking the conditions
    if arr[i] == arr[i + 1] and arr[i + 1] == arr[i + 2]:
        # printing the element as the
        # conditions are satisfied
        print(arr[i])