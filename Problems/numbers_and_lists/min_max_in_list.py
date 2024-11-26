# Method 1 - using max and min function
def find_min(lst: list) -> int:
    return min(lst)


def find_max(lst: list) -> int:
    return max(lst)


if __name__ == '__main__':
    lst = [65, 7,  78 , 89, 32, 21, 1, 77, 88, 99, 44, 345, 678]
    print(find_min(lst))
    print(find_max(lst))


# Method 2 - Without builtin functions
def find_min_max(lst: list):
    maximum = lst[0]
    minimum = lst[0]
    for i in range(len(lst)):
        if lst[i] > maximum:
            maximum = lst[i]
        if lst[i] < minimum:
            minimum = lst[i]
    return minimum, maximum


lst = [65, 7, 78, 89]
print(find_min_max(lst))



