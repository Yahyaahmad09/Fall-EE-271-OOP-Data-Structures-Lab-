# **2D Point class**

import math

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value: float) -> None:
        self._x = value

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value: float) -> None:
        self._y = value
    
    def distance_to(self, x, y ) -> float:
        return math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
    @property
    def distance_from_origin(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)


# Sub Class

class Point3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self._z = z

    @property
    def z(self) -> float:
        return self._z

    @z.setter
    def z(self, value: float) -> None:
        self._z = value
    
    def distance_to(self, x, y, z) -> float:
        return math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2)
    @property
    def distance_from_origin(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)






#-------------------------------------------------------------------------------------

# **Circle Class**

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        self._radius = value

    def volume(self, height: float) -> float:
        return self.area * height

    @property
    def area(self) -> float:
        from math import pi
        return pi * (self._radius ** 2)

    @property
    def circumference(self) -> float:
        from math import pi
        return 2 * pi * self._radius

    @property
    def diameter(self) -> float:
        return self._radius * 2
        
    @staticmethod
    def from_diameter(diameter: float):
        return Circle(diameter / 2)


# Sub Class

class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self._height = height

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        self._height = value

    @property
    def volume(self) -> float:
        return super().volume(self._height)

    @property
    def surface_area(self) -> float:
        return 2 * math.pi * self._radius * (self._radius + self._height)




#-------------------------------------------------------------------------------------

# **Rectangle class**

class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        self._width = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        self._height = value

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


# Sub Class

class Rhombus(Rectangle):
    def __init__(self, side_length, height) -> None:
        super().__init__(side_length, height)
        self.side_length = side_length
        self.height = height

    @property
    def side_length(self) -> float:
        return self.width

    @side_length.setter
    def side_length(self, value: float) -> None:
        self.width = value

    @property
    def area(self) -> float:
        return self.side_length * self.height

    @property
    def perimeter(self) -> float:
        return 4 * self.side_length




#-------------------------------------------------------------------------------------

# Rectangle

class Rectangle:
    """
    A class to represent a rectangle.
    """
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    @property
    def width(self) -> float:
        """Gets the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        """Sets the width of the rectangle."""
        self._width = value

    @property
    def height(self) -> float:
        """Gets the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        """Sets the height of the rectangle."""
        self._height = value

    @property
    def area(self) -> float:
        """Calculates the area of the rectangle."""
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        """Calculates the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

    def __repr__(self) -> str:
        """String representation of the rectangle."""
        return f'Rectangle(width={self.width}, height={self.height})'

# sub class

class Square(Rectangle):
    """
    A class to represent a square, inheriting from Rectangle.
    """
    def __init__(self, side: float) -> None:
        super().__init__(side, side)

    @property
    def side(self) -> float:
        """Gets the side length of the square."""
        return self.width

    @side.setter
    def side(self, value: float) -> None:
        """Sets the side length of the square."""
        self.width = value
        self.height = value

    def __repr__(self) -> str:
        """String representation of the square."""
        return f'Square(side={self.side})'





#-------------------------------------------------------------------------------------


# **Trapeoizd Class**

class Trapezoid:
    def __init__(self, base1: float = 1.0, base2: float = 1.0, height: float = 1.0) -> None:
        self.base1 = base1
        self.base2 = base2
        self.height = height

    @property
    def base1(self) -> float:
        return self._base1

    @base1.setter
    def base1(self, value: float) -> None:
        self._base1 = value

    @property
    def base2(self) -> float:
        return self._base2

    @base2.setter
    def base2(self, value: float) -> None:
        self._base2 = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        self._height = value

    @property
    def area(self) -> float:
        return ((self.base1 + self.base2) / 2) * self.height

    @property
    def perimeter(self) -> float:
        return self.base1 + self.base2 + 2 * self.height 


# Sub Class

class Parallelogram(Trapezoid):
    def __init__(self, base: float = 1.0, side: float = 1.0, height: float = 1.0) -> None:
        super().__init__(base, base, height)
        self.side = side

    @property
    def side(self) -> float:
        return self._side

    @side.setter
    def side(self, value: float) -> None:
        self._side = value

    @property
    def area(self) -> float:
        return self.base1 * self.height

    @property
    def perimeter(self) -> float:
        return 2 * (self.base1 + self.side)

