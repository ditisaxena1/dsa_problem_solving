from collections import Counter

string = "gangsofgangs"
new_dict = Counter(string)

odd_freq_chars = [i for i, j in new_dict.items() if int(j % 2 != 0)]
even_freq_chars = [i for i, j in new_dict.items() if int(j % 2 == 0)]

print(new_dict)
print(odd_freq_chars)
print(even_freq_chars)