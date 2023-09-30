# in JAVA, we should choose oe of them. abstraction or interface
# in Python, we can choose both methods.
import numbers


class Shape:  # this is base class.

    def __init__(self):
        self.name = type(self).__name__

    def area(self) -> numbers:  # abstract method. implementation is not mandatory
        pass

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'


class Square(Shape):

    def __init__(self, side):
        super().__init__()
        self.side = side


square = Square(5)
print(square)
print(square.area())
