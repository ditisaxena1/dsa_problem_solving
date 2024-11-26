# First Approach

def find_uncommon_words(str1, str2):
    uncommon_words = []
    str1 = str1.lower().split()
    str2 = str2.lower().split()
    for i in range(len(str1)):
        if str1[i] not in str2:
            uncommon_words.append(str1[i])

    for j in range(len(str2)):
        if str2[j] not in str1:
            uncommon_words.append(str2[j])

    return uncommon_words

print(find_uncommon_words(str1="I job in London and this is gold in london", str2="London london or gold Gold"))


# Second approach with better time complexity

def uncommon_words(sen1, sen2):
    sen1 = sen1.lower().split(" ")
    sen2 = sen2.lower().split(" ")

    print(sen1, sen2, sep="\n")

    set1 = set(sen1)
    set2 = set(sen2)

    uncommon = set1.symmetric_difference(set2)

    return uncommon

print(uncommon_words("happy I am", "I am the happy person"))
