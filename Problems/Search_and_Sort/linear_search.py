def linear_search(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            return True, f"{value} is present at index - {i}"
        else:
            continue

lst = [4,5,6,7,8,1,2,3]
value = 1

print(linear_search(lst, value))


