# First Approach

def max_sum(arr):
    max_sum = 0
    arr.sort()
    print(arr)
    for i in range(0, len(arr) - 2):
        temp = 0
        j = i
        while j < i+3:
            temp += arr[j]
            j += 1
        if max_sum < temp:
            max_sum = temp
            print(f"maximum sum at {i} is ", max_sum)

    return max_sum

print(max_sum([4,5,7,1,2]))


# Refined version of above approach
lst = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
lst = sorted(lst)
print(lst)

max_sum = 0

for i in range(len(lst)-2):
    sum1=0
    for j in range(i, i + 3):
        sum1 += lst[j]
    if sum1 > max_sum:
        max_sum = sum1

print(max_sum)
