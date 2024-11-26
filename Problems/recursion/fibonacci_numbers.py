def fibonacci_number(n):
    if n<=1:
        return n

    return fibonacci_number(n-1) + fibonacci_number(n-2)

print(fibonacci_number(6))

