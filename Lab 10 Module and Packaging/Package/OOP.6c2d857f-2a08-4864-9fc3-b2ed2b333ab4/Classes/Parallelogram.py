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
