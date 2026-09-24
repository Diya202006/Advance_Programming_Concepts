from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
 
class Circle(Shape):

    def area(self):
        radius = 5
        print("Area of Circle:", 3.14 * radius * radius)
 
c = Circle()
c.area()