from functools import reduce


def show_func(lst: list):
    result = reduce(lambda x, y: x + y, lst)
    return result

def filter1(lst):
    result = filter(lambda x: x==1, lst)
    return list(result)

print(show_func([1,2,3,4,5]))

print(filter1([1,2,3,4]))