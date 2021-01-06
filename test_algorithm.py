from algorithm import get_all_moves, evaluate, alp_bet, algorithm
from game_board import game_board
from moves import capture, push


def test_get_all_moves_Captures():
    board1 = [
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['o', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 'x', ' ', ' ', ' ', ' '],
        [' ', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
        [' ', 'x', ' ', 'o', ' ', 'o', ' ', 'o'],
        [' ', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
    ]
    board = game_board(board1)
    move3 = capture((7, 2), (5, 0))
    move1 = capture((5, 2), (3, 4))
    move2 = capture((5, 4), (3, 2))
    right_moves = [move1, move2, move3]
    moves = get_all_moves(board, 1)
    for i in range(len(right_moves)):
        assert right_moves[i].destination() == moves[i].destination()
        assert right_moves[i].origin() == moves[i].origin()


def test_get_all_moves_Pushes():
    board1 = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['o', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 'x', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 'x', ' ', ' ', ' ', ' '],
        [' ', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
        [' ', 'x', ' ', 'o', ' ', 'o', ' ', 'o'],
        [' ', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
    ]
    board = game_board(board1)
    move1 = push((2, 3), (3, 4))
    move2 = push((2, 3), (3, 2))
    move3 = push((6, 1), (7, 0))
    right_moves = [move1, move2, move3]
    moves = get_all_moves(board, 0)
    for i in range(len(right_moves)):
        assert right_moves[i].destination() == moves[i].destination()
        assert right_moves[i].origin() == moves[i].origin()


def test_evaluate_standard():
    board = game_board()
    assert evaluate(board, 1) == evaluate(board, 0) == 0


def test_evaluate_standard2():
    board1 = [
        [' ', 'O', ' ', ' ', ' ', ' ', ' ', ' '],
        ['o', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 'x', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 'x', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', 'x', ' ', ' ', ' ', 'o', ' ', 'o'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]
    board = game_board(board1)
    assert evaluate(board, 1) == evaluate(board, 0) == 39


def test_evaluate_o_won():
    board1 = [
        [' ', 'O', ' ', ' ', ' ', ' ', ' ', ' '],
        ['o', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', 'o', ' ', 'o'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]
    board = game_board(board1)
    assert evaluate(board, 0) == 1000000


def test_evaluate_x_won():
    board1 = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 'x', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 'x', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', 'x', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]
    board = game_board(board1)
    assert evaluate(board, 1) == -1000000


def test_evaluate_one_side_with_no_moves():
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
    assert evaluate(board, 0) == 1000000
    assert evaluate(board, 1) == 13


def test_alp_bet_standard():
    board1 = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 'x', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
        [' ', ' ', ' ', ' ', ' ', ' ', 'x', ' '],
        [' ', ' ', ' ', ' ', ' ', 'o', ' ', 'o'],
        [' ', ' ', ' ', ' ', 'o', ' ', ' ', ' '],
    ]
    board = game_board(board1)
    assert alp_bet(board, 0, 3) == 15


def test_algorithm():
    board1 = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', 'x', ' ', 'x', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', 'o', ' ', ' ', ' ', ' ', ' ', 'x'],
        [' ', ' ', ' ', ' ', ' ', ' ', 'x', ' '],
        [' ', ' ', ' ', ' ', ' ', 'o', ' ', 'o'],
        [' ', ' ', ' ', ' ', 'o', ' ', ' ', ' '],
    ]
    board = game_board(board1)
    assert algorithm(board, 0, 3) == (2, 1, 3, 2)
