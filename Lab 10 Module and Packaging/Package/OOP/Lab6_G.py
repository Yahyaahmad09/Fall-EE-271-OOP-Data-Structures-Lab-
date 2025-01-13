import math

class Point:
    def __init__(self, x: float = 0.0, y: float = 0.0):
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

    def distance_to(self, other: 'Point') -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def distance_from_origin(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def locate(self) -> str:

        return f"Point is located at ({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y})"

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"

    @staticmethod
    def origin() -> 'Point':
        return Point(0, 0)

    @classmethod
    def from_coordinates(cls, coordinates: tuple) -> 'Point':
        return cls(*coordinates)


#-------------------------------------------------------------------------------------


import math
class Circle:
    def __init__(self, radius: float = 1):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        self._radius = value

    def volume(self, height: float) -> None:
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

    @classmethod
    def unit_circle(cls) -> 'Circle':
        return cls(1)
    def __repr__(self) -> str:
        return f"Circle(radius={self._radius})"

    def __str__(self) -> str:
        return f"Circle with radius: {self._radius}"


#-------------------------------------------------------------------------------------



class Square:
    def __init__(self, side_length: float = 1.0) -> None:
        self.side_length = side_length
    @property
    def side_length(self) -> float:
        return self._side_length
    @side_length.setter
    def side_length(self, value: float) -> None:
        self._side_length = value
    @property
    def area(self) -> float:
        return self.side_length ** 2
    @property
    def perimeter(self) -> float:
        return 4 * self.side_length
    def __repr__(self) -> str:
        return f"Square(side_length={self.side_length})"
    def __str__(self) -> str:
        return f"Square with side length: {self.side_length}, area: {self.area}, perimeter: {self.perimeter}"


#-------------------------------------------------------------------------------------


class Rectangle:
    def __init__(self, width: float = 1.0, height: float = 1.0) -> None:
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

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

    def __str__(self) -> str:
        return f"Rectangle with width: {self.width}, height: {self.height}, area: {self.area}, perimeter: {self.perimeter}"

#-------------------------------------------------------------------------------------

import math
class Triangle:
    def __init__(self, a: float = 1.0, b: float = 1.0, c: float = 1.0) -> None:
        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self) -> float:
        return self._a

    @a.setter
    def a(self, value: float) -> None:
        self._a = value

    @property
    def b(self) -> float:
        return self._b

    @b.setter
    def b(self, value: float) -> None:
        self._b = value

    @property
    def c(self) -> float:
        return self._c

    @c.setter
    def c(self, value: float) -> None:
        self._c = value

    @property
    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    @property
    def perimeter(self) -> float:
        return self.a + self.b + self.c

    def __repr__(self) -> str:
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"

    def __str__(self) -> str:
        return (f"Triangle with sides: a={self.a}, b={self.b}, c={self.c}, "
                f"area: {self.area}, perimeter: {self.perimeter}")


#-------------------------------------------------------------------------------------
 # Traezoid

class Trapezoid:
    """A class which represent Trapezoid: A four-sided figure with at least one pair of parallel sides."""
    def __init__(self, base1: float = 1.0, base2: float = 1.0, height: float = 1.0) -> None:
        """To innitiate the class with given parameters"""
        self.base1 = base1
        self.base2 = base2
        self.height = height

    @property
    def base1(self) -> float:
        """To get the base1 of the Trapezoid"""
        return self._base1

    @base1.setter
    def base1(self, value: float) -> None:
        """To set the base1 of the Trapezoid"""
        self._base1 = value

    @property
    def base2(self) -> float:
        """To get the base2 of the Trapezoid"""
        return self._base2

    @base2.setter
    def base2(self, value: float) -> None:
        """To set the base2 of the Trapezoid"""
        self._base2 = value

    @property
    def height(self) -> float:
        """To get the heigth of the Trapezoid"""
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        """To set the heigth of the Trapezoid"""
        self._height = value

    @property
    def area(self) -> float:
        """To calculate the area of the Trapezoid"""
        return (self.base1 + self.base2) * self.height / 2

    @property
    def perimeter(self) -> float:
        """To calculate the perimeter of the Trapezoid"""
        raise NotImplementedError("Perimeter calculation requires lengths of non-parallel sides.")

    def __repr__(self) -> str:
        """Return the string  Representation of the Trapezoid"""
        return f"{type(self).__name__}(base1={self.base1}, base2={self.base2}, height={self.height})"

    def __str__(self) -> str:
        """Return the user_friendly  Representation  of  the Trapezoid"""
        return (f"Trapezoid with base1: {self.base1}, base2: {self.base2}")

#--------------------------------------------------------------------------------------------------------

# Parallelogram

class Parallelogram:
    """A class which represent Parallelogram: Where all sides are of equal length, but the angles are not necessarily 90 degrees."""
    def __init__(self, base: float = 1.0, height: float = 1.0) -> None:
        """To initiate the class and give parameters with default value"""
        self.base = base
        self.height = height

    @property
    def base(self) -> float:
        """To get the base of Parallelogram"""
        return self._base

    @base.setter
    def base(self, value: float) -> None:
        """To set the base of Parallelogram"""
        self._base = value

    @property
    def height(self) -> float:
        """"To get the heigth of Parallelogram"""
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        """To set the heigth of Parallelogram"""
        self._height = value

    @property
    def area(self) -> float:
        """To calculate the area of the Parallelogram"""
        return self.base * self.height

    @property
    def perimeter(self) -> float:
        """To calculate the perimeter of Parallelogram"""
        return 2 * (self.base + self.height)
    @classmethod
    def from_side_and_angle(cls, side: float, angle_degrees: float) -> 'parallelogram':
        """
        Create a Parallelogram instance given a side length and an angle between the sides.
        Parameters:
            side: The length of the side.
            angle_degrees: The angle between the sides in degrees.
        Returns:
            Parallelogram: A new instance of Parallelogram.
        """
        height = side * math.sin(math.radians(angle_degrees))
        return cls(base=side, height=height)   
    def __repr__(self) -> str:
        """Return the string  Representation of the Parallelogram"""
        return f"Parallelogram(base={self.base}, height={self.height})"
    def __str__(self) -> str:
        """Return the user_friendly  Representation  of  the Trapezoid"""
        return (f"Parallelogram with base: {self.base}, height: {self.height}")
