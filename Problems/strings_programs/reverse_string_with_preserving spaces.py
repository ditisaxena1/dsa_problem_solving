#  Brute force approach
def string_reverse_with_preserving_spaces(string):
    new_string = ''.join(reversed(string.replace(" ", '')))
    print(new_string)
    result = []
    index = 0
    for i in string:
        if i == ' ':
            result.append(' ')
        else:
            result.append(new_string[index])
            index += 1
    return ''.join(result)



print(string_reverse_with_preserving_spaces("Diti Saxena"))

# Better approach using left and right pointer

str = "India is big"
string= list(str)


left = 0
right = len(string)-1

while left <= right:
    if string[left] != " " and string[right] != " ":
        string[left], string[right] = string[right], string[left]
        left += 1
        right -= 1
    elif string[left] == " ":
        left += 1
    elif string[right] == " ":
        right -= 1

print("".join(string))