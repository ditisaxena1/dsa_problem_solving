""""
calculate sum of first n nubers using paramter in methods
"""

def sum_of_1st_n_num(S, N):
    if N == 0:
        print(S)
        return

    sum_of_1st_n_num(S+N, N-1)

sum_of_1st_n_num(0, 3)


"""
calculate sum of first n nubers using functional method and only one parameter that is the input number for which we need sum

"""

def sum_using_fucntion(n):
    if n == 0:
        return 0

    return n + sum_using_fucntion(n-1)

print(sum_using_fucntion(3))
