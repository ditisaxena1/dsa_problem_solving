def count_alpha(string):
    count = 0
    for char in string:
        if char.isalpha():
            count += 1
    print(count)

string = "Hello^& World!"
count_alpha(string)