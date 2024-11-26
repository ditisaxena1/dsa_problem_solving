"""
print N to 1 using recursion
"""

def print_numbers_without_loop(N):
    if N == 0:
        return
    else:
        print(N, end=" ")

    print_numbers_without_loop(N-1)


print_numbers_without_loop(5)

print("\n\n")
"""
print 1 to N using recursion
"""

def print_1_to_n(i, n):
    while i > n:
        return
    print(i, end=" ")

    print_1_to_n(i+1, n)

print_1_to_n(1, 5)


"""
print number where print line is after function call
1 to N print using backtrack 
"""
print("\n\n")
def recursion(i, N):
    if i == 0:
        return

    recursion(i-1, N)
    print(i, sep=" ")

recursion(5, 5)

