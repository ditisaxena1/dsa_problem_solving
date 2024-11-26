"""
LC Palindrome problem

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Input: s = "a.
Output: true

Input: s ="abc@"
Output: true


"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # string = ''.join(list(filter(lambda x: str(x) not in [' ', ',', ':'], s.lower())))
        left = 0
        right = len(s) - 1

        while left<right:
            if not s[left].isalpha():
                left += 1
            elif not s[right].isalpha():
                right -= 1
            elif s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True

ob = Solution()
print(ob.isPalindrome("A man, a plan, a canal: Panama"))