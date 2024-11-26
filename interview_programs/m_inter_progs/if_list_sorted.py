# Program is not correct

def is_list_sorted(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst)-1):
            if lst[j] > lst[j+1]:
                print("List is not sorted in ascending order")
                break
            elif lst[j+1]>lst[j]:
                print("List is not sorted in descending order")
                break

        break

is_list_sorted([1,2,3,4,6,7])
