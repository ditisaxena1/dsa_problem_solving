# Method 1 - use slicing
def is_palindrone(word):
    rev_word = word[::-1]
    if word == rev_word:
        return True, f"{word} is a palindrome"
    else:
        return False, f"{word} is not a palindrome"


string = "aha aha"
print(is_palindrone(string))

# Method 2 - no built in methods


def is_palindrome(word):
    i, j = 0, len(word) - 1
    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j -= 1
    return True

word = "radar"
print(is_palindrome(word))


# Method 3

def palindrome(word):
    reversed_word = ''
    for i in range(len(word)-1, -1, -1):
        reversed_word = reversed_word + word[i]
    if reversed_word == word:
        return True
    else:
        return False

word = "radar"
print(palindrome(word))







