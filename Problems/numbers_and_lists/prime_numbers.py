""""
making mistakes in loops. writing all the code with in while loop although under while only dividing and count increase should be there

"""
import math

# approach with while loop - brute force
for i in range(2,11):
    count = 0
    div = int(i//2)
    while div > 0:
        if i % div == 0:
            count += 1
        div -= 1
    if count == 1:
        print(i, end= " ")
    else:
        continue

print("\n\n")

"""
In below approach we check if count is 2 then prime. count will become 2 when number divides by itself and self. 
for evaluating self condition 
we have used if - > number // i != i and increment count by 2

"""

def prime_number(number):
    count = 0
    x = int(number**0.5)
    for i in range(1, x+1):
        if number % i == 0:
            count += 1
            # if number // i != i:
            #     count += 1

    if count == 1:
        return True
    else:
        return False

print(prime_number(17))

print("\n\n")


def if_prime_number(number):
    count = 0
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            count += 1
    if count == 0:
        return True
    else:
        return False

print(if_prime_number(17))

"""
print prime numbers in range 2-1000
"""

def prime_numbers():
    prime = []
    for num in range(2, 1001):
        div = int(math.sqrt(num))
        count = 0

        for d in range(1, div+1):
            if num%d == 0:
                count += 1
        if count == 1:
            prime.append(num)
    return prime


primes = prime_numbers()
print(primes)






