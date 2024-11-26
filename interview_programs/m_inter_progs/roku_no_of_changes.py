"""
if there is an array of words like ["add", "boook", "search"]

then if two consecutive letters are same in that case no of change will be 1

for example in "add" : two d are together hence no of change will be 1

in "boook: two o are together hence number of change is 1, after second o next o is followed by k hence no change

in "search" : none of the letters are together hence no of change 0

hence no of changes will be returned in a list as [1,1,0]

"""


lst = ["add", "booooook", "search"]

def no_of_changes(lst):
    no_of_changes = []
    for word in lst:
        count = 0
        j=0
        # for j in range(len(word)-1):
        while j < len(word)-1:
            if word[j] == word[j+1]:
                count += 1
                j += 2
            else:
                j += 1
        no_of_changes.append(count)

    return no_of_changes


print(no_of_changes(lst))




