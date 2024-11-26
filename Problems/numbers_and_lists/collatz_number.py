n= 3
while n != 1:
    if n % 2 == 0:
        print(int(n))
        n = n // 2

    else:
        print(int(n))
        n = (n * 3) + 1

    # n = 3 * n + 1 if n % 2 != 0 else n // 2