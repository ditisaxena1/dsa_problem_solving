"""
Given two strings 'str1' and 'str2', check if these two strings are isomorphic to each other.
If the characters in str1 can be changed to get str2, then two strings, str1 and str2, are isomorphic.
A character must be completely swapped out for another character while maintaining the order of the characters.
A character may map to itself, but no two characters may map to the same character.

Input:
str1 = aab
str2 = xxy
Output:
1
Explanation:
There are two different characters in aab and xxy, i.e a and b with frequency 2 and 1 respectively.


Input:
str1 = aab
str2 = xyz
Output:
0
Explanation:
There are two different characters in aab but there are three different charactersin xyz. So there won't be one to one mapping between str1 and str2.
"""

def is_isomorphic(str1, str2):

    len1, len2 = len(str1), len(str2)

    if len1 != len2:
        return False  # if length of two strings is not equal then not isomorphic

    char_map = {}
    char_visited_in_str2 = {}

    for i in range(len1):
        if str1[i] not in char_map:
            if str2[i] not in char_visited_in_str2:

                char_map[str1[i]] = str2[i]
                char_visited_in_str2[str2[i]] = True

            else:
                return False

        elif char_map[str1[i]] != str2[i]:
            return False
    return True


print(is_isomorphic('egg', 'geg'))




