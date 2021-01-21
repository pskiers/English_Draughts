from playerMaker import get_ai, create_player, create_2_players, get_depth
from unittest import mock
from players import Player

def test_get_depth(capsys):
    with mock.patch('builtins.input', return_value="4"):
        assert get_depth() == 4
    with mock.patch('builtins.input', return_value="7"):
        assert get_depth() == 7
        captured = capsys.readouterr()
        assert captured.out == "Warning: AI might take a long time to make a move\n"


def test_get_ai(capsys):
    with mock.patch('builtins.input', return_value="yes"):
        with mock.patch('playerMaker.get_depth', return_value=4):
            assert get_ai() == (1, 4)
    with mock.patch('builtins.input', return_value="no"):
        assert get_ai() == (0, 0)
    with mock.patch('builtins.input', return_value="asdfs"):
        assert get_ai() is None
        captured = capsys.readouterr()
        assert captured.out == "I don't understand\n"


def test_create_player():
    with mock.patch('playerMaker.get_ai', return_value=(1,4)):
        with mock.patch('builtins.input', return_value="andrzej"):
            assert create_player().ai() == 1
            assert create_player().name == 'Andrzej'


def test_create_2_players(capsys):
    guy = Player('adolf', 0)
    with mock.patch('playerMaker.create_player', return_value=guy):
        assert create_2_players() == (guy, guy)
        captured = capsys.readouterr()
        assert captured.out == "Create player who goes second\nCreate player who goes first\n"
