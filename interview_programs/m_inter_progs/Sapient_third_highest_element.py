def nth_highest_element(lst, n):
    for i in range(len(lst)):
        for j in range(0, len(lst)-1):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

        print(f"list is after {i} iteration is ", lst)
        # if i == n-1:
        #     return lst[n-1]

    return lst, lst[n-1]

lst = [9,4,5,7,1,2,8,3,6]
n = 3

print(nth_highest_element(lst, n))
