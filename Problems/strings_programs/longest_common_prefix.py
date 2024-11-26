"""
Given an array of strings strs[]. The task is to return the longest common prefix among each and every strings present in the array.
If there’s no prefix common in all the strings, return “-1”.

Examples:

Input: strs[] = [“geeksforgeeks”, “geeks”, “geek”, “geezer”]
Output: gee
Explanation: “gee” is the longest common prefix in all the given strings.

Input: strs[] = [“hello”, “world”]
Output: -1
Explanation: There’s no common prefix in the given strings.

"""

# Brute Force Approach - Using Sort

def longest_common_prefix(strs):
    strs.sort()

    first_wrd = strs[0]
    last_wrd = strs[-1]

    count = 0
    smallest_wrd = ""

    if len(first_wrd) <= len(last_wrd):
        smallest_wrd = first_wrd
    else:
        smallest_wrd = last_wrd

    for i in range(len(smallest_wrd)):
        if first_wrd[i] == last_wrd[i]:
            count += 1
        else:
            break

    if count == 0:
        return ""
    else:
        return smallest_wrd[:count]


print(longest_common_prefix(["geeksforgeeks", "geeksforgee", "geeks", "geeksfor"]))
print(longest_common_prefix(["dog","racecar","car"]))

