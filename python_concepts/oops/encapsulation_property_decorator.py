""""
property decorator has three functionalities - getter, setter and deleter
property makes a method behave like attribute and can be accessed by the object without the use of paranthesis

getter gives the ability to fetch the value
setter gives the ability to set the value or do some other manipulations around it
and deleter deletes the values

In summary, @property makes methods behave like attributes, allowing for more control and cleaner code when getting, setting, or deleting values in a class.
"""

class Circle:
    def __init__(self, radius):
        self.__radius = radius  # Private attribute

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self.__radius = value

    @radius.deleter
    def radius(self):
        del self.__radius

# Example usage
c = Circle(5)
print(c.radius)  # Accesses the getter method, Output: 5

c.radius = 10    # Calls the setter method to set a new value
print(c.radius)  # Output: 10

del c.radius