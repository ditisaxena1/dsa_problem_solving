def find_substring(string, substring):
    if substring in string:
        print(string.index(substring))
        return True
    else:
        return False

string = "Geeks for Geeks"
substring = "Geeks"
print(find_substring(string, substring))


# return all substring of a string
"""
abc - O/P
a
b
c
ab
bc
abc
"""

def find_all_substring(string):
    length = len(string)
    for i in range(0, length):
        for j in range(length-i):
            k = i+j
            for n in range(j, k+1):
                print(string[n], end="")
            print()

string = "abc"
find_all_substring(string)
























