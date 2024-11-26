def index_count_of_1(string):
    count = 0
    index = -1
    for i in range(len(string)):
        if string[i] =='1':
            count += 1
            if index == -1:
                index = i + 1
        elif string[i] == '0':
            if count > 0:
                print(f"Index- {index} and Count- {count}", end="\n")
            index = -1
            count = 0

    if count > 0:
        print(f"Index-{index} and Count-{count}", end="\n")

string = "11110011011101110111"
index_count_of_1(string)
