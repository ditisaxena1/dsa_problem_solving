import os

# path of the given file
print(os.path.dirname(os.path.abspath("file.txt")))

# current working directory
print(os.path.abspath(os.getcwd()))

print(os.listdir())
"""
Use abspath() method to get an absolute path.
getcwd() gives the current working directory.
"""
print(os.path.abspath(os.getcwd()))

print(os.getcwd())