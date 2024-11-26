"""
Input String = "aaabbbcccaaa
Output String = "a3b3c3a3"
"""


def string_compress(string):
    i = 0
    while i < len(string):
        count = 0
        current_char = string[i]
        while i < len(string) and string[i] == current_char:
            count+= 1
            i += 1
        print(current_char, count, sep="", end="")


string_compress("aaabbbaaaaa")






