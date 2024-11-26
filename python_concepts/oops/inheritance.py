"""Python code to demonstrate how parent constructor are called.
"""
class Person(object):

    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)


# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)


# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using its instance
a.display()


print("\n\n")
"""
constructor overriding using super
"""

class Person(object):

    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)


# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
    #  this below method if used then object of employee will call this display
    # def display(self):
    #     print(self.salary)



# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using its instance
a.display()

print("\n\n")
"""
accessing private member of parents class

Private member cannot be accessed and leads to attribute error. 
Protected member can be accessed

"""


# Python program to demonstrate private members
# of the parent class

class C(object):
    def __init__(self):
        self.c = 21

        # d is private instance variable
        self.__d = 42

        # f is protected member
        self._f = 44


class D(C):
    def __init__(self):
        self.e = 84
        C.__init__(self)


object1 = D()

# produces an error as d is private instance variable
print(object1.c)
print(object1._f)

print(object1.__d)