string = "110100001010101"
lst = list(string)

count = 0
for i in range(len(lst)):
    if lst[i] == "0":
        count += 1
print(count)

for i in range(count):
    lst[i] =0
print(lst)

for i in range(count, len(lst)):
    lst[i] = 1
print(lst)


