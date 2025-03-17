from abc import ABC, abstractmethod
import math



class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass



class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
        
        
        
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
        
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
        
        
        
    def area(self):
        # формулата съм я взел от https://en.wikipedia.org/wiki/Heron%27s_formula
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    def perimeter(self):
        return self.a + self.b + self.c


circle = Circle(8)
rectangle = Rectangle(8, 6)
triangle = Triangle(3, 4, 5)




print(f"Area of Circle: {circle.area()}")
print(f"Perimeter of Circle: {circle.perimeter()}")
print(f"Area of Rectangle: {rectangle.area()}")
print(f"Perimeter of Rectangle: {rectangle.perimeter()}")
print(f"Area of Triangle: {triangle.area()}")
