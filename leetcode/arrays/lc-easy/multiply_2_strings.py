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

# this approach is not good for medium level and will not work with input with non digit inputs. Need to recode

class Solution(object):
    def multiply(self, num1, num2):
        # res1 = any(ch.isdigit for ch in num1)
        # res2 = any(ch.isdigit for ch in num2)
        # if res1 == True and res2 == True:

        product = str(int(num1)*int(num2))
        return product

ob = Solution()
num1 , num2 = "2", "3"
print(ob.multiply(num1, num2))