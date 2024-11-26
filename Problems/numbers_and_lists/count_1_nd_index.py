string = "111000110000111"
string = list(string)
print(string)
count = 0
for i in range(len(string)):
    if string[i] == "1":
        count += 1
    elif string[i] == "0":
        if count>0:
            print(f"the number of times 1 occurs is {count}")
        count = 0
if count > 0:
    print(f"the number of times 1 occurs is {count}")

def print_indices_and_counts(s):
    count = 0
    index = -1
    for i, char in enumerate(s):
        if char == '1':
            count += 1
            if index == -1:
                index = i + 1
        else:
            if count > 0:
                print(f"{index},{count}")
                count = 0
                index = -1
    if count > 0:
        print(f"{index},{count}")

# Example usage
s = "0011110001100"
print_indices_and_counts(s)
