"""
finally block has break statement - in this case exception will not be reraised and finally block will take precedence over the raise statement
"""

for i in range(3):
    try:
        if i == 1:
            raise ValueError("An error occurred!")
    except ValueError as e:
        print(f"Exception caught: {e}")
        raise
    finally:
        print(f"Finally block for iteration {i}")
        if i ==1:
            break

"""
finally block with comtinue statement -- in this case exception will not be reraised and finally block will take precedence over the raise statement and print statement will also get skipped
"""
print("\n\n")
for i in range(3):
    try:
        if i == 1:
            raise ValueError("An error occurred!")
    except ValueError as e:
        print(f"Exception caught: {e}")
        raise
    finally:
        print(f"Finally block for iteration {i}")
        if i == 1:
            continue
    print(f"End of iteration {i}")


"""
return in finally block -- When return is used in the finally block, it will override any return statement in the try or except block, 
and any exception that might have been raised will not be re-raised. The value returned will be the one from the finally block
"""


print("\n")
def example():
    try:
        raise ValueError("An error occurred!")
    except ValueError as e:
        print(f"Exception caught: {e}")
        return "From except block"
    finally:
        print("Finally block")
        return "From finally block"

print(example())