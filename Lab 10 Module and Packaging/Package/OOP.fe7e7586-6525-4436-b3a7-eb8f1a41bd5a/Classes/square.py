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
