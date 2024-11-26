"""
Used different approaches to solve setence reverse and string reverse

Best approach is at last
"""

# Method 1 = reverse sentence
def reverse_words(sentence):
    reversed_sentence = ''
    words = sentence.lower().split()
    for word in words:
        reversed_sentence = word + ' ' + reversed_sentence
    print(reversed_sentence)


sentence = "I love Python"
reverse_words(sentence)

# Method 2 - use reversed function
sentence = "I love python"
reversed_sentence = ' '.join(reversed(sentence.split()))
print(reversed_sentence)

# Method 3 - reverse each word of sentence
sentence = "I love python"
words = sentence.split()
new_sentence = ''
for word in words:
    reversed_word = ''.join(reversed(word))
    new_sentence = new_sentence + ' ' + reversed_word

print(new_sentence)

# Method 4 - reverse each word of sentence and reverse the sentence as well
sentence = "I love python"
words = sentence.split()
new_sentence = ''
for word in words:
    reversed_word = ''.join(reversed(word))
    new_sentence = reversed_word + ' ' + new_sentence

print(new_sentence)

# Method 5 - use slicing

sentence ="I love python"
print(sentence[::-1])

# Method 6 - Optimized - using 2 pointer approach -- left and right index
print("\n")
str = "I love India"

words = str.split(" ")
new_string = []
for word in words:
    if len(word) == 1:
        new_string.append(word)
    else:
        temp = list(word)
        left = 0
        right = len(word)-1
        while left <= right:
            temp[left], temp[right] = temp[right], temp[left]
            left += 1
            right -= 1
        new_string.append("".join(temp))

print(" ".join(new_string))

