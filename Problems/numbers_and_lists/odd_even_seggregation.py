def odd_or_even_seggregation(lst):
    even_list =[]
    odd_list = []

    if not lst:
        return False
    for i in lst:
        if i%2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    return even_list, odd_list


lst = [5,8,1,2,4,5,122,98,97,90,44,43,37]
print(odd_or_even_seggregation(lst))