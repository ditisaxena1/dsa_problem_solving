
def sumOfDivisors(N):
    factors = []
    for i in range(1, N + 1):

        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                factors.append(j)
                if i // j != j:
                    factors.append(i // j)

    return sum(factors)


print(sumOfDivisors(3))