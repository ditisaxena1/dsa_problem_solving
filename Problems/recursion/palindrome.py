"""

palindrome using recursion
"""

def is_palindrome(i, string):
    if i >= len(string)//2:
        return
    elif string[i] != string[len(string)-i-1]:
        return False
    else:
        is_palindrome(i+1, string)
        return True

string = "MADAM"
print(is_palindrome(0, string))




