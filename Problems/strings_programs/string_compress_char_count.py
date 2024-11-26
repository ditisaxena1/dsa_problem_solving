"""

aaabb
O/P - 3a2b
"""
from collections import Counter


def char_count(string):
    i = 0
    while i < len(string):
        count = 0
        char = string[i]
        while i < len(string) and string[i] == char:
            count += 1
            i += 1
        print(count, char, sep="", end="")


char_count('aaabbaa')

print()

def string_compress_with_dictionary(string):
    new_dict = Counter(string)
    for i,j in new_dict.items():
        print(i, j, sep="", end="")

string_compress_with_dictionary('aaabbsdqwqaabbccdnsaksjaks')
