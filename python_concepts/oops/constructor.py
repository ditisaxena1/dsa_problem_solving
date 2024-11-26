class MyClass:
    def __init__(self, name=None):
        if name is None:
            print("Default constructor called")
        else:
            self.name = name
            print("Parameterized constructor called with name", self.name)

    def method(self):
        # I can pass anything as second argument in place of name, it just expects a second string argument
        if hasattr(self, 'name'):
            print("Method called with name", self.name)
        else:
            print("Method called without a name")





# Create an object of the class using the default constructor
obj1 = MyClass()

# Call a method of the class
obj1.method()

# Create an object of the class using the parameterized constructor
obj2 = MyClass("John")

# Call a method of the class
obj2.method()


