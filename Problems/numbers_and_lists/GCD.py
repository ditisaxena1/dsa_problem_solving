def gcdOfTwoNumbers(number1, number2):
    factors1 = []
    factors2 = []

    for i in range(1, number1+1):
        if number1 % i == 0:
            factors1.append(i)

    for i in range(1, number2 + 1):
        if number2 % i == 0:
            factors2.append(i)
    print(factors1, factors2, sep="\n\n")

    common_factors = set(factors1).intersection(factors2)
    print(max(list(common_factors)))


gcdOfTwoNumbers(12,9)


# second aproach - better than above

def gcd(number1, number2):
    gcd = 1
    for i in range(1, max(number1, number2)+1):
        if number1 % i == 0 and number2 % i == 0:
            gcd = i

    return gcd


print("GCD is")
print(gcd(11, 13))


# using algorithm Euclidean Algo
"""
using euclidean theorem we can find the GCD

"""

def gcd_using_euclidean(number1, number2):
    while number1 > 0 and  number2> 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1

    if number1 == 0:
        return number2
    else:
        return number1

print(gcd_using_euclidean(12, 13))








