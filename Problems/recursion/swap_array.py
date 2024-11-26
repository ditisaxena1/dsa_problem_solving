"""
using recurion to swap an array.
will use two pointer aproach - left and right elements.

"""


# def swap(left, right, array):
#     array[left], array[right] = array[right], array[left]


def swap_array(left, right, array):
    if left >= right:
        return
    array[left], array[right] = array[right], array[left]
    return swap_array(left+1, right-1, array)


array = [1,2,3,4,5,6,7,8,9]
swap_array(0, len(array)-1, array)
print(array)

"""
using recursion with using two arguments.
if left is i then right will be n-i-1


"""

def second_aproach_swap(i, N, array):
    if i >= N//2:
        return
    # swap(i, N-i-1, array)
    array[i], array[N-i-1] = array[N-i-1], array[i]
    return second_aproach_swap(i+1, N, array)


array = [1,2,3,4,5,6,7,8,9]
second_aproach_swap(0, len(array), array)
print(array)

