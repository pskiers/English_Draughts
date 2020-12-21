from typing import Tuple
from Errors import (
    CoordinatesNotOnTheBoardError,
    ChosenWitheSquareError
)


class move:
    """
    """
    def __init__(self, move_from: Tuple[int, int], move_to: Tuple[int, int]):
        x1, y1 = move_from
        self.set_origin(x1, y1)
        x2, y2 = move_to
        self.set_destination(x2, y2)

    def set_origin(self, new_x: int, new_y: int):
        if 8 > new_x > -1 or 8 > new_y > -1:
            raise CoordinatesNotOnTheBoardError()
        elif new_x % 2 == new_y % 2:
            raise ChosenWitheSquareError()
        else:
            self._origin = (new_x, new_y)

    def set_destination(self, new_x: int, new_y: int):
        if 8 > new_x > -1 or 8 > new_y > -1:
            raise CoordinatesNotOnTheBoardError()
        elif new_x % 2 == new_y % 2:
            raise ChosenWitheSquareError()
        else:
            self._destination = (new_x, new_y)

    def origin(self):
        return self._origin

    def destination(self):
        return self._destination


class push(move):
    pass


class capture(move):
    pass
