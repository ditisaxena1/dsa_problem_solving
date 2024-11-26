"""
# We have a function that looks for 'missing items' in a list of strings,
# of the form "some_base_string_X" where X is an integer number.
# We are looking for numbers that are missing from the input.
# For instance, with 'foo_1', 'foo_3', that is missing 'foo_2'.
# However, based on issues reported by customers,
# it seems like this code has some bugs in it.

# Review the code to identify any bugs you can find, and test fixes for them.
"""
"""

def find_missing(the_list):
    base_string = the_list[0][:-1]


    start_number = int(the_list[0][-1])
    print("start number", start_number)


    last_number = start_number

    missing = []
    
    for item in the_list[1:]:
        expected_number = last_number + 1
        actual_number = int(item.replace(base_string, ''))
        if expected_number != actual_number:

            missing.append(base_string + str(expected_number))

            last_number = actual_number

    return missing

TESTS = [
    # Format: (Input(List), Expected Output(List))
    (['foo_1'], []),
    (['foo_1', 'foo_2'], []),
    (['bar_1', 'bar_3'], ['bar_2']),
    (['foo_1', 'foo_2', 'foo_', 'foo_4', 'foo_6'], ['foo_3', 'foo_5'])
]

"""

""" 
My code

Things I covered:

Handling Empty List:
correctly checked for an empty list with if not the_list:.

Extraction of Last Numbers:
identified and collected the numbers from the strings.

Identifying Missing Numbers:
used a loop to identify which numbers were missing from the sequence.

"""

def find_missing(the_list):

    if not the_list:
        return -1

    last_numbers = []
    missing = []
    for i in range(len(the_list)):
        number = the_list[i][-1]
        if not number.isdigit():
            pass
        else:

            last_numbers.append(int(number))

    print("the last numbers--", last_numbers)

    for i in range(1, last_numbers[-1]+1):
        if i not in last_numbers:
            base_string = the_list[0][:-1] + str(i)
            missing.append(base_string)

    return missing

print(find_missing(['foo_1', 'foo_2', 'foo_', 'foo_4', 'foo_6']))

"""
Area for improvement

Handling Multi-digit Numbers:

Your code uses the_list[i][-1] to extract the number, which only works for single-digit numbers. If the number in the string is '12', for example, this would incorrectly extract '2'.
Fix: You should use a more robust method to extract the numeric part, such as splitting the string on the underscore (_) and taking the part after it.
Incorrect base_string Handling:

You used the_list[0][:-1] + str(i) to form the missing strings. This is incorrect because it assumes the base string always ends in a single digit, which may not be the case.
Fix: Use rsplit('_', 1)[0] to correctly slice the base string before the last underscore, ensuring it works for strings like 'foo_12'.
Skipping Non-Digit Characters:

You simply skipped over non-digit characters, which is good. However, you could improve the code by raising an exception or logging a warning if the input data isn't in the expected format.
Edge Cases:

Your solution doesn't handle cases where the list is unordered, strings have multi-digit numbers, or there are gaps greater than one in the sequence.
Fix: Consider sorting the last_numbers list before identifying missing numbers.
"""


def find_missing(the_list):
    if not the_list:
        return -1

    last_numbers = []
    missing = []
    base_string = None

    for item in the_list:
        parts = item.rsplit('_', 1)
        if len(parts) == 2 and parts[1].isdigit():
            number = int(parts[1])
            last_numbers.append(number)
            if base_string is None:
                base_string = parts[0] + '_'
        else:
            # If the format is incorrect, you can choose to log a warning or raise an error.
            continue

    if not last_numbers:
        return -1  # If no valid numbers were found

    last_numbers.sort()
    for i in range(last_numbers[0], last_numbers[-1]+1):
        if i not in last_numbers:
            missing.append(f"{base_string}{i}")

    return missing

print(find_missing(['foo_3', 'foo_5', 'foo_2', 'foo_1']))


# Corrected code written by me

def findMissing(input_list):

    if len(input_list) == 0:
        return -1
    base_string = None

    last_numbers = []
    missing_item = []
    for item in input_list:
        split_item = item.rsplit('_', 1)
        if len(split_item) == 2 and split_item[1].isdigit():
            last_numbers.append(int(split_item[1]))
            if base_string is None:
                base_string = split_item[0] + "_"
        elif not split_item[1].isdigit():
            return -1

    last_numbers.sort()

    for i in range(1, last_numbers[-1]+1):
        if i not in last_numbers:
            # missing = base_string + str(i)
            missing_item.append(f"{base_string}{i}")

    return missing_item

print(findMissing(['foo_1', 'foo_2', 'foo_7', 'foo_4', 'foo_6']))


