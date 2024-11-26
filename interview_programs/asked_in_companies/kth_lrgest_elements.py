""""
Find the top K largest hashtag#elements from a large dataset of integers.
"""

def kth_lrgest_elements(lst, k):
    lst = sorted(lst, reverse=True)
    return lst[:k]

lst = [3, 2, 1, 5, 6, 4]
k = 2

print(kth_lrgest_elements(lst, k))