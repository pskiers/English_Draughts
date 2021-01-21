from playerMaker import get_ai, create_player, create_2_players, get_depth
from unittest import mock
from players import Player


def test_get_depth(capsys, mocker):
    with mock.patch('builtins.input', return_value="4"):
        assert get_depth() == 4
    with mock.patch('builtins.input', return_value="7"):
        assert get_depth() == 7
        captured = capsys.readouterr()
        msg = "Warning: AI might take a long time to make a move\n"
        assert captured.out == msg
    with mock.patch('builtins.input', side_effect=['asd', 0, 3]):
        assert get_depth() == 3
        captured = capsys.readouterr()
        msg = "Plese enter a number\nDepth cannot be equal to less than 1\n"
        assert captured.out == msg


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


def test_create_player(capsys, mocker):
    with mock.patch('playerMaker.get_ai', return_value=(1, 4)):
        with mock.patch('builtins.input', return_value="andrzej"):
            assert create_player().ai() == 1
            assert create_player().name == 'Andrzej'
    with mock.patch('playerMaker.get_ai', return_value=(0, 0)):
        with mock.patch('builtins.input', side_effect=['asd12', "andrzej"]):
            andrzej = create_player()
            assert andrzej.ai() == 0
            assert andrzej.name == 'Andrzej'
            captured = capsys.readouterr()
            assert captured.out == "That is not a name\n"


def test_create_2_players(capsys):
    guy = Player('adolf', 0)
    with mock.patch('playerMaker.create_player', return_value=guy):
        assert create_2_players() == (guy, guy)
        captured = capsys.readouterr()
        msg = "Create player who goes second\nCreate player who goes first\n"
        assert captured.out == msg
