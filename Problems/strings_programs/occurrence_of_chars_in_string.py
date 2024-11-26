from collections import Counter
# Method 1 - using dictionary
string = "dgfhiijk"
char_count = dict()
for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)

# Method 2 - using counter from collections
char_count = Counter(string)
new_list = [(i,j) for i,j in char_count.items()]
print(new_list)
print(char_count)


"""
I/O - aabbccccdddee
O/P - a2b2c4d3e2
"""

string = "aabbccccdddee"
char_count = Counter(string)
# way 1 to print
for i,j in char_count.items():
    print(i,end="")
    print(j,end="")
# way 2 to print
print("\n")
compressed_string = ""
for char, count in char_count.items():
    compressed_string += char + str(count)

print(compressed_string)

# chatgpt method
def compress_string(input_string):
    if not input_string:
        return input_string

    compressed = ""
    current_char = input_string[0]
    count = 1

    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            compressed += current_char + str(count)
            current_char = input_string[i]
            count = 1

    compressed += current_char + str(count)

    return compressed

input_string = "aabbccccdddee"
compressed_string = compress_string(input_string)
print(compressed_string)


# different way using filter

# The original input string

OriginalString = "The quick brown fox jumps over the lazy dog."

# Splitting the string and removing spaces and punctuation.
CleanedString = ''.join(filter(lambda x: x.lower().isalpha() and x != " ", OriginalString.split()))

# To Bring Consistency in the string, converting everything to lowercase
CleanedString = CleanedString.lower()

# dictionary comprehension for the frequency count&nbsp;
result = {x: CleanedString.count(x) for x in CleanedString}

# Printing the result dictionary
print(result)