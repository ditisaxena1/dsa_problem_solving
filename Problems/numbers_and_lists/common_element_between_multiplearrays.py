#  need to correct this

def find_commons(arrays):
    all_sets = [set(array) for array in arrays]
    all_ele = set.union(*all_sets)
    common_ele = set.intersection(*all_sets)
    print(all_ele)
    print(common_ele)

    # uncommon_ele = set.difference(*all_sets)
    uncommon_ele = all_ele - common_ele
    return uncommon_ele

array1 = [1, 2, 3, 2, 1,5]
array2 = [2,3,4]
array3 = [1,2,3]
print(find_commons([array1, array2, array3]))


"""
Input: A[] = {1, 5, 10, 20, 30} , B[] = {5, 13, 15, 20}, C[] = {5, 20} 
Output: 5 20
Explanation: 5 and 20 are common in all the arrays.

Input: A[] = {1, 5, 10, 20, 30}, B[] = {5, 13, 15, 20}, C[] = {5, 20} 
Output: 5
Explanation: 5 occurs multiple times in all the three arrays but it will be printed once.

"""

A = [1, 5, 10, 20, 30]
B = [5, 13, 15, 20, 1]
C = [1, 5, 20]
D = []

if len(A) > (len(B) and len(C)):
    bigger = A
elif len(B) > (len(A) and len(C)):
    bigger = B
else:
    bigger = C

for num in A:
    if num in B and num in C:
        D.append(num)

print(D)
