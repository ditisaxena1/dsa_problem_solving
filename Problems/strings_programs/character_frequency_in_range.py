"""
I/P = "abce"
range is a to e

O/P - [1,1,1,0,1]

Use approach of Ascii value


"""


def countCharacterFrequencies(s):
    # Initialize a frequency array of size 8 (for 'a' to 'h')
    freq = [0] * 8

    # Count the frequencies of each character in the string
    for char in s:
        print(ord(char))
        if 'a' <= char <= 'h':
            freq[ord(char) - ord('a')] += 1

    # Build the output based on the frequency array
    output = []
    for i in range(8):
        output.append(str(freq[i]))

    # Convert the output list to a string
    return ' '.join(output)


# Example usage
s = "aabcdeh"
result = countCharacterFrequencies(s)
print(result)  # Output should be "2 1 1 1 1 0 0 1"