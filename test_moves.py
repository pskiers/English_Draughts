import pytest
from moves import move, push, capture
from Errors import (
    CoordinatesNotOnTheBoardError,
    ChosenWitheSquareError,
    NotAPushMoveError,
    NotACaptureMoveError,
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


def test_createPush():
    someMove = push((1, 2), (2, 3))
    assert someMove.origin() == (1, 2)
    assert someMove.destination() == (2, 3)


def test_createBadPush():
    with pytest.raises(NotAPushMoveError):
        push((1, 2), (3, 4))


def test_createCapture():
    someMove = capture((1, 2), (3, 4))
    assert someMove.origin() == (1, 2)
    assert someMove.destination() == (3, 4)


def test_createBadCapture():
    with pytest.raises(NotACaptureMoveError):
        capture((1, 2), (2, 3))
