def count_unique_elements(lst: list) -> list:
    unik_list = []
    for num in lst:
        if num not in unik_list:
            unik_list.append(num)

    print("Total Unique elements -", len(unik_list))
    return unik_list

print(count_unique_elements([1,1,2,2]))