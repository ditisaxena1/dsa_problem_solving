"""
Question: Write a Java Program to achieve the desired output, where each occurrence of the letter "o" is replaced with an increasing number of dollar signs ($),
Input String = "Go to Joho"
Output String = "G$ t$$ J$$$h$$$$"
"""

def add_dollar(string):
    final_strng = []
    count = 1
    for char in string:
        if char == "o" or char == "O":
            final_strng.append("$" * count)
            count += 1
        else:
            final_strng.append(char)

    return "".join(final_strng)

print(add_dollar("Go to Joho"))