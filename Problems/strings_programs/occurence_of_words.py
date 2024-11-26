# Method 1 - using counter
from collections import Counter
from itertools import count


def occurence_of_words(sentence):
    words = sentence.lower().split()
    word = Counter(words)
    return word


sentence = input("Enter a sentence: ")
print(occurence_of_words(sentence))

# Method 2 - using simple dictionary to display frequency of all words


def count_words(sentence):
    word_dict = {}
    for word in sentence.lower().split():
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    # to display frequency of each word
    return f"the word count dictionary is {word_dict}"


sentence =input("Enter a sentence: ")
print(count_words(sentence))

# Method 3 - display only duplicate words


def count_words(sentence):
    word_dict = {}
    for word in sentence.lower().split():
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    # to display more than one duplicate
    duplicate_words = [(word, cnt) for word, cnt in word_dict.items() if cnt > 1]
    return duplicate_words


sentence =input("Enter a sentence: ")
print(count_words(sentence))



