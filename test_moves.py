import pytest
from moves import move
from Errors import (
    CoordinatesNotOnTheBoardError,
    ChosenWitheSquareError
)


def test_createMove():
    someMove = move((1, 2), (2, 3))
    assert someMove.origin() == (1, 2)
    assert someMove.destination() == (2, 3)


def test_createBadMove1():
    with pytest.raises(CoordinatesNotOnTheBoardError):
        move((1, 8), (2, 3))


def test_createBadMove2():
    with pytest.raises(ChosenWitheSquareError):
        move((1, 3), (2, 3))
