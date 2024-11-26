def string_reverse_space_preserved(string):
    rev_string = ''.join(reversed(string.replace(" ",'')))
    new_string = []
    index=0

    for i in string:
        if i == ' ':
            new_string.append(' ')
        else:
            new_string.append(rev_string[index])
            index += 1

    return ''.join(new_string)

print(string_reverse_space_preserved('Hello in the world'))





