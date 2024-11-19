# Practice: Exercise 1 from https://thartmanoftheredwoods.github.io/CIS-12/week_13pyCh15.html

# Exercise 1: Write a class Rectangle that includes methods to calculate area and perimeter.
# Implement __str__ for string representation.
# You should include an init method that receives a width and height.

class Rectangle:
    """draws rectangles from input width and height"""

    def __init__(self,width,height):
        self.width = width
        self.height = height
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")

    def find_area(self):
        area = self.width * self.height
        return area

    def find_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter

    def __str__(self):
        return f'For rectangle with a width of {self.width} and a height of {self.height},\n the area would be {self.find_area()} and the perimeter would be {self.find_perimeter()}.'

#testing
rect1 = Rectangle(12,10)
rect2 = Rectangle(5,6)
#print(rect1)

