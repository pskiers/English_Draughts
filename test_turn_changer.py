from turn_changer import change_turn
from game_board import game_board
from moves import push, capture


def test_turn_after_push():
    board1 = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
        [' ', ' ', ' ', ' ', ' ', ' ', 'x', ' '],
        [' ', ' ', ' ', ' ', ' ', 'o', ' ', 'o'],
        [' ', ' ', ' ', ' ', 'o', ' ', ' ', ' '],
    ]
    board = game_board(board1)
    move = push((7, 6), (6, 5))
    assert change_turn(1, board, 0, move) == 0


def test_turn_after_promotion():
    board1 = [
        [' ', ' ', ' ', 'O', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', 'x', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
        [' ', ' ', ' ', ' ', ' ', ' ', 'x', ' '],
        [' ', ' ', ' ', ' ', ' ', 'o', ' ', 'o'],
        [' ', ' ', ' ', ' ', 'o', ' ', ' ', ' '],
    ]
    board = game_board(board1)
    move = capture((2, 1), (0, 3))
    assert change_turn(1, board, 1, move) == 0


def test_turn_after_capture_nocombo():
    board1 = [
        [' ', ' ', ' ', 'O', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', 'x', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', 'o', ' ', 'x'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', 'o', ' ', ' '],
        [' ', ' ', ' ', ' ', 'o', ' ', ' ', ' '],
    ]
    board = game_board(board1)
    move = capture((6, 7), (4, 5))
    assert change_turn(1, board, 0, move) == 0


def test_turn_after_capture_combo():
    board1 = [
        [' ', ' ', ' ', 'O', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', 'x', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', 'x', ' '],
        [' ', ' ', ' ', ' ', ' ', 'o', ' ', 'x'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', 'o', ' ', ' '],
        [' ', ' ', ' ', ' ', 'o', ' ', ' ', ' '],
    ]
    board = game_board(board1)
    move = capture((6, 7), (4, 5))
    assert change_turn(1, board, 0, move) == 1
