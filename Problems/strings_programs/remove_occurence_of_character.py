# Method 1
def remove_occurence_of_character(string, char):
    new_str = ''
    if not string:
        return False
    elif len(string) >= 1:
        for i in range(len(string)):
            if not string[i] == char:
                new_str += string[i]
            else:
                continue

    return new_str


print(remove_occurence_of_character(string="hello world hello and hi", char="h"))

# Method 2
def remove_chars_with_method(string, char):
    string = string.replace(char, '')
    return string


print(remove_chars_with_method(string="hello world", char="he"))

def remove_char_using_list_comprehension(string, char):
    string = ''.join([i for i in string if i not in char])
    return string


print(remove_char_using_list_comprehension(string="hello world", char="llo"))


def remove_chars_from_in_same_str(string, char):
    string = list(string)

    for i in range(len(string)):
        if string[i] == char:
            string[i] =""

    return ''.join(string)

print(remove_chars_from_in_same_str(string="hello world", char="h"))


