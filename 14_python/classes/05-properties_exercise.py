# Consider the following Python code:

# @dataclass
# class Circle:
#   _radius: float

#   # TODO: Add properties to this class

# # Create an instance of Circle
# circle = Circle(5)

# # Test the properties
# print("Radius:", circle.radius)
# circle.radius = 10
# print("Diameter:", circle.diameter)
# print("Area:", circle.area)
# print("Circumference:", circle.circumference)

# Add properties to the class so that the test code runs correctly. Don't forget to include appropriate type annotations!
from dataclasses import dataclass
from math import pi



@dataclass
class Circle:
    _radius: float


    @property
    def radius(self) -> float:
        return self._radius
    
    @radius.setter
    def radius(self, value: int | float) -> None:
        self._radius = value

    @property
    def diameter(self) -> int | float:
        return self.radius * 2
    
    @property
    def area(self)-> int | float:
        return pi * (self._radius ** 2)
    
    @property
    def circumference(self)-> int | float:
        return (2 * pi) * self._radius
    

def main()-> None:
    circle = Circle(5)

    # Test the properties
    print("Radius:", circle.radius)
    circle.radius = 10
    print("Diameter:", circle.diameter)
    print("Area:", circle.area)
    print("Circumference:", circle.circumference)


if __name__ == "__main__":
    main()