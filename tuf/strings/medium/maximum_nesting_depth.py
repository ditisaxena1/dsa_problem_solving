"""
Find maximum depth of nested parenthesis in a string
We are given a string having parenthesis like below
     “( ((X)) (((Y))) )”
We need to find the maximum depth of balanced parenthesis, like 4 in the above example. Since ‘Y’ is surrounded by 4 balanced parentheses.
If parenthesis is unbalanced then return -1.

Examples :

Input : S = "( a(b) (c) (d(e(f)g)h) I (j(k)l)m)";
Output : 4

Input : S = "( p((q)) ((s)t) )";
Output : 3

Input : S = "";
Output : 0

Input : S = "b) (c) ()";
Output : -1

Input : S = "(b) ((c) ()"
Output : -1
"""

# Brute Force - Correct in case of balanced strings
def maximum_nesting_depth(string):

    if len(string) == 0:
        return 0

    depth = 0
    maxi = 0

    for c in string:
        if c == '(':
            depth += 1
            maxi = max(maxi, depth)
        elif c == ')':
            depth -= 1
    return maxi


print(maximum_nesting_depth("( p((q)) ((s)t) )"))