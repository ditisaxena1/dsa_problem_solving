class Counter:

    count = 0

    def __init__(self):

        Counter.count += 1

    @classmethod

    def get_count(cls):

        return cls.count

# Creating instances of the class

c1 = Counter()

c2 = Counter()

c3 = Counter()

# Accessing the class attribute using the class method

print("Count:", Counter.get_count())