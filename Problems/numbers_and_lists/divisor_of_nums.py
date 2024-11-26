# Using basic for loop and range
def get_divisors(number):
    for i in range(1, number):
        if number % i == 0:
            print(i)


get_divisors(36)

print("\n\n")
# using sqrt approach

def get_divisors(number):
    for i in range(1, int(number**0.5)+1):
        if number % i == 0:
            print(i)
            if number // i != i:
                print(number // i)

get_divisors(36)




