"""
Brute Force Approach
Tc is roughly Big O(n^3) or O(n^2)
"""
def find_max_length(lst):
    max_len = 0
    target = 3
    length = 0

    for i in range(len(lst)):
        sum = 0
        for j in range(i, len(lst)):
            sum += lst[j]
            if sum == target:
                length = max(length, j-i+1)
    return length

print(find_max_length([2,1,1,1,0,0]))





