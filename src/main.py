from typing import Union

class Calculator:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def divide(self) -> Union[int, float]:
        return self.x / self.y

    def add(self) -> Union[int, float]:
        return self.x + self.y