
def transpose_matrix(matrix):
    # Calculate the number of rows and columns in the original matrix
    rows = len(matrix)
    cols = len(matrix)
    transposed_matrix =[]
    # Create a new matrix with swapped dimensions
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]
    print(transposed_matrix)


    # Iterate through each element in the original matrix
    for i in range(rows):
        for j in range(cols):
            # Swap the row and column indices to transpose the element
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)


# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original matrix:")
print_matrix(matrix)

print("Transposed matrix:", transpose_matrix(matrix))