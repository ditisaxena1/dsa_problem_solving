"""

check Armstrong number or not
"""

def if_armstrong_number(number):
    arm_num = 0
    org_num = number

    while number > 0:
        digit = number % 10
        arm_num += digit ** 3
        number = number // 10

    if arm_num == org_num:
        return arm_num, True
    else:
        return arm_num, False


print(if_armstrong_number(127))