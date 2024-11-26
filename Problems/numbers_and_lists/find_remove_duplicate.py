from collections import Counter


def find_dup(array):
    new_dict = Counter(array)
    new_list = [i for i,j in new_dict.items() if j > 1]
    return new_list


def find_nondup(array):
    new_dict = Counter(array)
    new_list = [i for i,j in new_dict.items() if j == 1]
    return new_list


def rem_duplicates(array):
    # new_list = []
    # [new_list.append(i) for i in array if i not in new_list]
    # return new_list
    new_list = []
    for i in array:
        if i not in new_list:
            new_list.append(i)
    return new_list



array = [2,2,4,5,6,2,4]
print(find_dup(array))
print("\n")
print(find_nondup(array))
print("\n")
print(rem_duplicates(array))


"""
display item with frequency of greater than k
Input : test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3 
Output : [4, 3] 
Explanation : Both elements occur 4 times. 

Input : test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6], K = 2 
Output : [4, 3, 6] 
Explanation : Occur 4, 3, and 3 times respectively.
"""

def elements_freq_greater_than_k(array, k):
    new_dict = Counter(array)
    elements_with_freq_gr_than_k = [i for i, j in new_dict.items() if j > k]
    return elements_with_freq_gr_than_k

print(elements_freq_greater_than_k([4, 6, 4, 3, 3, 4, 3, 4, 3, 8], 3))


