new_list =set()
list1= [3,4,6,7,1,2,9]
list2= [1,10,11,12,6,8,0]

for i in range(len(list1)):
    if list1[i] in list2:
        new_list.add(list1[i])
    else:
        continue
print(new_list)

# second way for arrays of different length
list1= [3,4,6,7,1,2,9]
list2= [1,10,11,12,6,8,7,6]
new_list =set()
if len(list1)>len(list2):
    small_arr, big_arr = list2, list1
else:
    small_arr, big_arr = list1, list2

for element in small_arr:
    if element in big_arr:
        new_list.add(element)
    else:
        continue
print(new_list)



