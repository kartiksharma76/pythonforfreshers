class Shape:
    def area(self):
        print("Area of shape")

class Circle(Shape):
    def area(self):
        print("Area of circle")

class Square(Shape):
    def area(self):
        print("Area of square")

for obj in [Circle(), Square()]:
    obj.area()