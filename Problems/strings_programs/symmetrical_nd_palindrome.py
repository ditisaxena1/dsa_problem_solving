def is_symmetrical(string):
    mid = int(len(string)//2)
    left_str = string[:mid]
    if int(len(string) % 2) == 0:
        right_str = string[mid:]
    else:
        right_str = string[mid+1:]

    if left_str == right_str:
        return "Yes, It is Symmetrical"
    else:
        return "No, It is not Symmetrical"

def is_palindrome(string):
    left = 0
    right = len(string)-1
    flag = True
    while left <= right:
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            flag = False
            break

    if flag == True:
        return "Yes, it is a palindrome"
    else:
        return "No, it is a palindrome"

string = input("Enter a string: ")
print(is_symmetrical(string))
print(is_palindrome(string))






