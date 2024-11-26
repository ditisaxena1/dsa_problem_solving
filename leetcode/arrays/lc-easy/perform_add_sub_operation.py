def perform_add_sub_operation(operations):
    X = 0
    for i in operations:
        if i in ['++X', 'X++']:
            X += 1
        elif i in ['--X', 'X--']:
            X -= 1

    return X

print(perform_add_sub_operation(['--X','X++','X++']))


