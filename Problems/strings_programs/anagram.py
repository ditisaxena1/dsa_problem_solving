def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False, f"`str1` and `str2` are not tha anagrams as length is not same"
    elif sorted(str1) == sorted(str2):
        return True, f"`str1` and `str2` are the anagrams"
    else:
        return False, f"`str1` and `str2` are not anagrams"


str1 = "rrrrrr"
str2 = "tttttt"

print(is_anagram(str1, str2))


