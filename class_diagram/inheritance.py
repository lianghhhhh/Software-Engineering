class Shape:
    def __init__(self):
        self.area = 0
        self.name = "Shape"
        
    def print_area(self):
        print(f"This {self.name}'s area is: {self.area}")

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.name = "Circle"
        self.radius = radius
        self.area = 3.14 * radius * radius 

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.name = "Rectangle"
        self.width = width
        self.height = height
        self.area = width * height

if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    circle.print_area()      # Output: This Circle's area is: 78.5
    rectangle.print_area()   # Output: This Rectangle's area is: 24