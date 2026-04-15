from abc import ABC, abstractmethod

# Abstract Class
class Shape(ABC):

    # Abstract Method
    @abstractmethod
    def area(self):
        pass

# Child Class
class Circle(Shape):
    def area(self):
        print("Area of Circle")

class Square(Shape):
    def area(self):
        print("Area of Square")

# Object Creation
c = Circle()
s = Square()

c.area()
s.area()