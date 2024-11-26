from functools import reduce

word = "Python vowel"
vowels = "aeiou"

# find vowel in the string "Python"
result = [char for char in word if (char not in vowels) and (char != " ")]

print(result)



numbers = [1, 2, 3, 4, 5]

# create a new list using list comprehension
square_numbers = [num * num for num in numbers]

print(square_numbers)

# Output: [1, 4, 9, 16, 25]

"""
list comprehension example for sum of even numbers
"""

numbers = [1, 2, 3, 4, 5]
even = [num for num in numbers if num%2 == 0]
print(sum(even))
