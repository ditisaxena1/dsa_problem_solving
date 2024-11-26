"""

you have a four digit number. Lets suppose 2932 so there are 4 digits - 2 occurs 2 times, 9 occurs 1 time and 3 occurs 1 time.
so the lowest 2 digit number would be such that all 4 digits should be used such that their sum is mimimum of all other combos.

trick : create a list, sort the numbers, and add numbers at position 0-2 and 1-3 to get lowest possible numbers
"""

def minimumSum(num):
    """
    :type num: int
    :rtype: int
    """
    num = str(num)
    print(num)
    num = [int(i) for i in num]
    print(num)
    num.sort()
    print(num)
    num1 = str(num[0]) + str(num[2])
    num2 = str(num[1]) + str(num[3])
    return int(num1) + int(num2)

print(minimumSum(2932))