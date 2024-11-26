"""
Reduce string by removing outermost parentheses from each primitive substring

Given a string S of valid parentheses “(“ and “)”, the task is to print the string obtained by removing the outermost parentheses of every primitive substring from S.
Input: S = “(()())(())()”
Output: ()()()
Explanation: The input string is “(()())(())()” can be decomposed into primitive substrings “(()())” + “(())”+”()”.
After removing outermost parentheses of each primitive substrings, the string obtained is “()()” + “()” = “()()()”

Input: S = “((()())(())(()(())))”
Output: (()())(())(()(()))
"""

def remove_outermost_paranthesis(string):

    result = ""
    opening_bracket = 0
    closing_bracket = 0
    index = 0
    for i in range(len(string)):
        if string[i] == '(':
            opening_bracket += 1
        elif string[i] == ')':
            closing_bracket += 1
        if opening_bracket == closing_bracket:
            result += string[index+1:i]
            index = i+1

    return result

print(remove_outermost_paranthesis("(()())(())()"))


