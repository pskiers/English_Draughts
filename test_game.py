from game import game
from game_board import game_board
from moves import push, capture


def test_createAGame():
    board = game_board()
    game1 = game(board)
    assert game1.gameboard() == board.board()


def test_makeAPush():
    board = game_board()
    game1 = game(board)
    assert game1.gameboard() == board.board()
    move = push((5, 0), (4, 1))
    game1.make_a_push(move)
    board2 = [
        [' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['x', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', 'o', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
        [' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o'],
        ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
    ]
    assert game1.gameboard() == board2
