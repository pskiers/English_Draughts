from players import Player
import pytest
from Errors import InvalidNameError


def testCreateAHumanPlayer():
    someGuy = Player('andrzej', 0)
    assert someGuy.name == 'Andrzej'
    assert someGuy.ai() == 0
    assert someGuy.depth == 0


def testCreateAnAIPlayer():
    someGuy = Player('andrzej', 1, 4)
    assert someGuy.name == 'Andrzej'
    assert someGuy.ai() == 1
    assert someGuy.depth == 4



def testCreateABadPlayer():
    with pytest.raises(InvalidNameError):
        Player('asd dsf', 0)
