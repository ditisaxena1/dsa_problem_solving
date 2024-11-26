from itertools import combinations, permutations


def three_digit_num_all_combo(num: list):

    perm = permutations(num, 3)
    comb = combinations(num, 3)
    for n in perm:
        print(n)
    print("\n")
    for n in comb:
        print(n)

three_digit_num_all_combo([1,2,3])

print("\n\n")
def permu(array):
    for i in range(len(array)):
        for j in range(len(array)):
            for k in range(len(array)):
                if i!=j and i!=k and j!=k:
                    print(array[i], array[j], array[k])

permu([0,9,5])