from collections import Counter


def remove_dup_chars(string):
    if not string:
        return False
    elif len(string) == 1:
        return string
    elif len(string) >1:
        char_count = dict()
        for char in string:
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
        # char_count = Counter(string)
        print(char_count)
        new_string = [i for i,j in char_count.items() if j==1]
        if new_string:
            return ''.join(new_string)
        else:
            return "All characters are duplicate"


print(remove_dup_chars('ffik'))

