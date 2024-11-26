"""
perform read , write and append operation

"""
# readlines reads lines as a list, readline reads one line
with open("file.txt", "r") as content:
    data = content.readline()
    print(data)

print("\n\n")

with open("file.txt", "r") as read:
    read_data = read.readlines()
    print(read_data)

print("\n\n")
# read - reads all lines in the file as is

with open("file.txt", "r") as read:
    read_only = read.read()
    print(read_only)


# write and writelines
with open("write.txt", 'w') as write_file:
    content = write_file.writelines(read_only)


with open("write.txt", 'r') as read_file:
    data = read_file.read()
    print(data)

with open("write.txt", 'w') as write_file:
    data = write_file.write("Diti")


# append operation
with open("write.txt", 'a') as append_file:
    append_file.write(" ")
    append_file.write("Saxena")

print("\n\n")
# write data for content read using readlines which is a list format and not string

with open("write_new.txt", "w") as write_new:
    for line in read_data:
        write_new.write(line)

with open("write_new.txt", 'r') as read_file:
    data = read_file.read()
    print(data)

