"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"

"""


class Solution(object):
    def multiply(self, num1, num2):
        product = 0
        if num1.isdigit() is True and num2.isdigit() is True:

            product = str(int(num1)*int(num2))

            return product

        else:
            return False

ob = Solution()
num1 , num2 = "123", "456"
print(ob.multiply(num1, num2))