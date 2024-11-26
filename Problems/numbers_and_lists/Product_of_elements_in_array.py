""""
If input array is [1,2,3,4]
then the  output should be the array which has product of the elements in array -- [24, 23, 8, 6]
"""


def product(array):
    new_array = array.copy()
    product_array = []
    for i in range(len(array)):
        product = 1
        for j in range(len(new_array)):
            if i != j:
                product *= new_array[j]
        product_array.append(product)

    return product_array

print(product([1,2,3,4]))