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