dictionary = dict()
print(type(dictionary))

dictionary[1] = 'Geeks'
dictionary[2] = [1,2,3]

print(dictionary)

print(dictionary.get(2))

"""
nested dictionary
"""

Dict = {'Dict1': {1: 'Geeks'},
        'Dict2': {'Name': 'For'}}

print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])

"""
delete dictionary
"""
del Dict['Dict1']
print(Dict)

print("\n\n")
"""
all basic dict operations
"""
dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}
dict2 = dict1.copy()
print(dict2)
dict1.clear()
print(dict1)
print(dict2.get(1))
print(dict2.items())
print(dict2.keys())
dict2.pop(4)
print(dict2)
dict2.popitem()
print(dict2)
dict2.update({3: "Scala"})
print(dict2)
print(dict2.values())
