# Method 1 - use slicing

string = "america"
reversed_string = string[::-1]
print(reversed_string)

# Method 2 - use method reversed and loop over the iterator object
string = "diti"
reversed_string = reversed(string)
for char in reversed_string:
    print(char, end='')

# Method 3 - use reversed and join function
string = "diti"
reversed_string = ''.join(reversed(string))
print(reversed_string)

# Method 4 - without using inbuilt methods


def reversed_string(string):
    reverse = ''
    for i in range(len(string)):
        reverse = string[i] + reverse
    return reverse


string = "mokobara"
print(reversed_string(string))

# Method 5 - 2 pointer approach

string = "Diti"
string = list(string)
left = 0
right = len(string)-1
while left < right:
    string[left], string[right] = string[right], string[left]
    left += 1
    right -= 1

print(string)



