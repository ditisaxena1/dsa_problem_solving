def if_binary_string(string):
    # length = len(string)
    # binary_length = 0
    # for i in range(length):
    #     if string[i] == '0' or string[i] == '1':
    #         binary_length += 1
    #     else:
    #         binary_length = 0
    # if binary_length == length:
    #     return True
    # else:
    #     return False
    return string.count('1') + string.count('0') == len(string)

string = '111001010101011'
print(if_binary_string(string))