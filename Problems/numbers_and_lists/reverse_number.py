"""
Reverse a number and return the same.
if a number has trailing zeroes then eliminate zero.
I/P = 10400 O/P = 401

"""

def count_digit(number):
    count = 0
    while number > 0:
        count += 1
        number = number // 10
    return count

print(count_digit(23401))


def reverse_number(number):
    rev_numb = 0
    while number > 0:
        digit = number % 10
        rev_numb = (rev_numb * 10) + digit
        number = number // 10

    return rev_numb

print(reverse_number(10400))


