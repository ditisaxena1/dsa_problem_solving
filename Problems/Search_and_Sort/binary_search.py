lst = [1,2,3,4,5,6,7,8,9,10]
left = 0
right = len(lst) - 1
value = 11
while left <= right:
    mid = (left + right) // 2
    if lst[mid] == value:
        print("Found")
        break
    elif lst[mid] < value:
        left = mid + 1
    elif lst[mid] > value:
        right = mid - 1
else:
    print("Not found")






















