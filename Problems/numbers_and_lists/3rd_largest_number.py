"""
find the 3rd largest element in an array
 I/P = [1,2,3,4,5]
 3rd largest: 3
"""
#  Brute force approach using sets
def find_3rd_largest(lst: list):
    unique_list = list(set(lst))
    return unique_list[-3]

print(find_3rd_largest([1,2,1,5,6,7,8,4,5,7,7,8]))






