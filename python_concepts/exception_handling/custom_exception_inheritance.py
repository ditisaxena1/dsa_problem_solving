class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")


class MyException(Exception):
    "this will print the exception message"
    def __init__(self):
        print(" I am an exception")


for i in range(1):
    try:
        raise MyException()
    # Here it will work if we except MyException or Exception as MyException is derived from exception
    except Exception as e:
        print("Error")
    finally:
        print("finally")

for i in range(1):
    try:
        raise MyException()
    # Here it will not Except this and exception will be raised
    except NameError as e:
        print("Error")
    finally:
        print("finally")





