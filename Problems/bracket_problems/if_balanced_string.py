def is_balanced(string):
    stack = []
    for char in string:
        if char in ['(', '[', '{']:
            stack.append(char)
        else:
            if stack and ((stack[-1] == '(' and char == ')') or (stack[-1] == '{' and char == '}') or (stack[-1] == '[' and char == ']')):
                stack.pop()
            else:
                return False
    return not stack


expression = "{}}"

if is_balanced(expression):
    print("it is a balanced")
else:
    print("it is not balanced")



# My own approach
def if_balanced(string):
    opening_brackets = ["(", "{", "["]
    stack = []
    for i in string:
        if i in opening_brackets:
            stack.append(i)
        elif i.isalnum():
            pass
        elif i not in opening_brackets:
            if stack and ((i == ")" and stack[-1] == "(") or (i == "]" and stack[-1] == "[") or (i == "}" and stack[-1] == "{")):
                stack.pop()
            else:
                return False

    if not stack:
        return True, "Balanced"


print(if_balanced("{((uu))}"))









































