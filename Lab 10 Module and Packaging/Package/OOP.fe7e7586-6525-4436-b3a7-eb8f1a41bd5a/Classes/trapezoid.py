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
