"""
Problem Statement: You are given a positive integer n. Your task is to find and return its square root. If ‘n’ is not a perfect square, then return the floor value of 'sqrt(n)'.

Note: The question explicitly states that if the given number, n, is not a perfect square, our objective is to find the maximum number, x, such that x squared is less than or equal to n (x*x <= n).
In other words, we need to determine the floor value of the square root of n.

Input Format:
 n = 28
Result:
 5
Explanation:
 Square root of 28 is approximately 5.292. So, the floor value will be 5.
"""
# Normal Approach - it is a Optimal Approach

import math
number = 28
print(math.floor(math.sqrt(number)))

print(int(28**0.5))




# using linear search
def sqrt_of_number(n):
    ans = 1
    for i in range(1, n):
        if i*i <= n:
            ans = i

    return ans


print(sqrt_of_number(28))


# Using BInary search
def sqrt_of_number_in_logn(n):
    low, high = 1, n
    ans = 1
    while low <= high:
        mid = (low+high)//2

        if mid*mid <= n:
            ans = mid
            low = mid+1
        else:
            high = mid-1

    return ans

print(sqrt_of_number_in_logn(28))