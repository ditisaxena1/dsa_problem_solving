missing_values = []
array = [1,2,3,5,7,8,9,11,12,13,14,40,80,90,100]

for i in range(array[0], array[-1]+1):
    if i not in array:
        missing_values.append(i)
    else:
        continue
print(missing_values)






