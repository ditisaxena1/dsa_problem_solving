"""
Two strings str1 and str2 are called isomorphic if there is a one-to-one mapping possible for every character of str1 to every character of str2.
And all occurrences of every character in ‘str1’ map to the same character in ‘str2’.

Examples:

Input:  str1 = “aab”, str2 = “xxy”
Output: True
Explanation: ‘a’ is mapped to ‘x’ and ‘b’ is mapped to ‘y’.

Input:  str1 = “aab”, str2 = “xyz”
Output: False
Explanation: One occurrence of ‘a’ in str1 has ‘x’ in str2 and other occurrence of ‘a’ has ‘y’.
"""

# Brute Force

def isomorphic(str1, str2):

    n1 = len(str1)
    n2 = len(str2)

    if n1 != n2:
        return False

    char_map = dict()  # for character mapping between string 1 and string 2
    char_viz = dict() # for marking true/false if char in string2 is already added to the dictionary

    for i in range(n1):
        if str1[i] not in char_map:
            if str2[i] not in char_viz:

                char_map[str1[i]] = str2[i]
                char_viz[str2[i]] = True

            elif char_viz[str2[i]] == True:
                return False

        else:
            if char_map[str1[i]] != str2[i]:
                return False

    return True

print(isomorphic("gaa", "egg"))





