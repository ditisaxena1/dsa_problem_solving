from functools import reduce

#  using for loop
def multiply_list_products(array):
    product = 1
    for i in range(len(array)):
        product *= array[i]

    return product

print(multiply_list_products([2,3,4]))

# Reduce and Lambda usage
a = reduce(lambda x, y: x * y, [1,2,3])

print(a)
