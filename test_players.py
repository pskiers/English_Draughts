from players import Player
import pytest
from Errors import InvalidNameError


def testCreateAHumanPlayer():
    someGuy = Player('andrzej', 0)
    assert someGuy.name == 'Andrzej'
    assert someGuy.ai() == 0


def testCreateABadPlayer():
    with pytest.raises(InvalidNameError):
        Player('asd dsf', 0)
