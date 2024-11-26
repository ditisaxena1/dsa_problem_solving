'''
* * * * *
* * * *
* * *
* *
*
'''

rows = 5
for row in range(1, rows+1, 1):
    for col in range(0, rows-row+1, 1):
        print("*",end=" ")
    print()
#    2nd method - better
# rows = 5
# for row in range(rows):
#     for col in range(rows, row, -1):
#         print("*", end=" ")
#     print()


'''
*
* *
* * *
* * * *
* * * * *
'''
print("\n")
rows = 5
for row in range(1, rows+1, 1):
    for col in range(0, row, 1):
        print("*",end=" ")
    print()

'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
print("\n")
print()
rows = 5
for row in range(1, rows+1, 1):
    for col in range(1, rows+1, 1):
        print("*",end=" ")
    print()
print("\n\n")
# Second approach
for i in range(5):
    print('* ' * 5, end="\n")

'''
     *
    * *
   * * *
  * * * *
 * * * * *    
'''
print("\n\n")
rows = 5
for row in range(1, rows+1, 1):
    for col in range(0, rows-row, 1):
        print(" ", end=" ")
    for col in range(0, row, 1):
        print(" * ", end=" ")
    print()

'''
    *
   **
  ***
 ****
*****
'''

print("\n\n")
rows = 5
for row in range(1, rows+1, 1):
    for col in range(0, rows-row, 1):
        print(" ", end=" ")
    for col in range(0, row, 1):
        print("*", end=" ")
    print()


'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

print("\n")

for row in range(1, rows+1):
    """
    solved this using two approach. 
    commented out is the lengthy one and uncommented is short and direct
    """
    # num = 1
    # for col in range(0, row):
    #     print(num, end=" ")
    #     num += 1
    # print()
    for col in range(1, row+1):
        print(col, end=" ")
    print()

    
'''
12345
1234
123
12
1
'''
rows = 5
print("\n\n")
for row in range(rows):
    num = 1
    for col in range(rows, row, -1):
        print(num, end=" ")
        num += 1
    print()

# second approach
for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()


"""
    *
   ***
  *****
 *******
*********
"""

rows = 5
for row in range(1, rows+1):
    for col in range(0, rows-row):
        print(" ", end="")
    for col in range(0, 2*row-1):
        print("*", end="")
    print()


"""
 *********
  *******
   *****
    ***
     *
"""
print("\n\n")
for i in range(rows, 0, -1):
    for col in range(rows-i):
        print(' ',end='')
    for col in range((i*2)-1):
        print('*',end='')

    print()

""""
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

"""

print("\n\n")
rows = 9
lower = rows//2
upper = rows - lower
for row in range(upper):
    for col in range(0, row+1):
        print("*", end=" ")
    print()
for row in range(lower):
    for col in range(lower-row):
        print("*", end=" ")
    print()

"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""

print("\n\n")
rows = 5
num = 1
for row in range(rows):
    for col in range(0, row+1):
        print(num, end=" ")
        num +=1
    print()


"""
1
22
333
4444
55555
"""

print("\n\n")
for i in range(1, rows + 1):
    for j in range(i):
        print(i, end=" ")
    print()

"""
A 
B C 
D E F 
G H I J 
K L M N O

"""

print("\n\n")
char = "A"
num = 65
for i in range(0, rows):
    for j in range(0, i+1):
        print(chr(num), end=" ")
        num += 1
    print()

"""
A
A B
A B C
A B C D
A B C D E
"""

print("\n\n")
char = "A"
num = 65
for i in range(0, rows):
    for j in range(0, i+1):
        print(chr(num), end=" ")
        num += 1
    num = 65
    print()

"""
A
B B
C C C
D D D D
E E E E E
"""

print("\n\n")
num = 65

for i in range(0, rows):
    for j in range(0, i+1):
        print(chr(num), end=" ")
    num += 1

    print()

"""
A B C D E
A B C D
A B C
A B
A
"""

print("\n\n")
num = 65

for i in range(0, rows):
    for j in range(rows-i):
        print(chr(num), end=" ")
        num += 1
    num = 65

    print()

"""
E
D E
C D E
B C D E
A B C D E
"""
print("\n\n")
num = 69

for i in range(1, rows+1):
    for j in range(1, i+1):
        print(chr(num), end=" ")
        num += 1
    num = 69
    num -= i

    print()

""""
   A
  ABC
 ABCDE
ABCDEFG   

"""
print("\n\n")
n_rows = 4
num = 65
for i in range(1,n_rows+1):
    for j in range(n_rows-i):
        print(" ", end="")
    for j in range((i*2)-1):
        print(chr(num), end="")
        num += 1
    num=65
    print()


"""
    A                  
   ABA
  ABCBA
 ABCDCBA 

"""
print("\n\n")
n_rows = 4
num = 65
for i in range(n_rows):
    for j in range(n_rows-i-1):
        print(" ", end="")
    for j in range(i+1):
        print(chr(num), end="")
        num += 1
    num = 65
    print()


print("\n\n")





















