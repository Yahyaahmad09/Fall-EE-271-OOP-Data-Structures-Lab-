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
