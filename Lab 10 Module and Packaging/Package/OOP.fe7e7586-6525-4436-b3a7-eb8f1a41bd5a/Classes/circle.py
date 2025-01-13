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
