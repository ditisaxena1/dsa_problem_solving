"""
Functionality of maps and filter
The map() function in Python takes in a function and an iterable (lists, tuples, and strings) as arguments.
"""
# MAP
result = map(lambda x: x * 2, [1,2,3,4])
print(list(result))

# FILTER
result = filter(lambda x: x%2==0, [1,2,3,4])
print(list(result))