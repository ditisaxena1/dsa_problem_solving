# Factorial
def factorial(n):
    fact = 1
    while n > 0:
        fact = fact * n
        n = n - 1
    return fact


print(factorial(6))

# Fibonacci
print("\n")
number = 8
num1 = 0
num2 = 1
print(num1, num2, sep='\n')
while number > 0:
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    number -= 1
    print(num3)

# Fibonacci part 2
print("\n\n")
size_of_series = 8
num_to_find = int(input())
f1,f2=1,1
temp =0
lst = [f1,f2]
if size_of_series == 1:
    print(f1)
elif size_of_series == 2:
    print(lst)
else:
    while (size_of_series > 2):
        temp=f1+f2
        f1=f2
        f2=temp
        lst.append(f2)
        size_of_series -= 1
print(lst)
print(lst[num_to_find - 1])





