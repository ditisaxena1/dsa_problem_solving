def count_words(sentence, word):
    count = 0
    words = sentence.lower().split()
    for i in range(len(words)):
        if words[i] == word:
            count += 1
    return f"the word {word} appears {count} times"


sentence = "I am a Geeks for geeks"
word = "geeks"
num = count_words(sentence, word)
print(num)
