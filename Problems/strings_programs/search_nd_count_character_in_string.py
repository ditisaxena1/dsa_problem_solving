def count_character_in_string(word, character):
    character_count = 0
    for i in range(len(word)):
        if word[i] == character:
            character_count += 1
    return f"the number of occurrence of '{character}' is {character_count}"

word = "fhjgkjdgksjgcsdkjchgsdkjcgdshjgc hfhgfhfhj drstarea gjhgkjgk"
character = "f"
print(count_character_in_string(word, character))

# the time complexity will be O(n)