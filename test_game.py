from game import game
from game_board import game_board
from moves import push, capture
import pytest
from Errors import (
    PawnMovingBackwardsError,
    SquareTakenError,
    CapturingNothingError,
    CapturingYourOwnPiceError,
    NoPieceOnTheSquareError,
    NotAMoveError,
)


def test_createAGame():
    board = game_board()
    game1 = game(board)
    assert game1.gameboard() == board.board()


def test_just_move():
    board = game_board()
    game1 = game(board)
    assert game1.gameboard() == board.board()
    game1.just_move(5, 0, 4, 1, 0)
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


def test_just_bad_move():
    board = game_board()
    game1 = game(board)
    assert game1.gameboard() == board.board()
    with pytest.raises(SquareTakenError):
        game1.just_move(6, 1, 5, 0, 0)


def test_standard_move_an_o():
    board = game_board()
    game1 = game(board)
    assert game1.gameboard() == board.board()
    game1.move_an_o(5, 0, 4, 1, 0)
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


def test_move_an_o_to_king():
    board1 = [
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['o', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
        [' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o'],
        ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
    ]
    board = game_board(board1)
    game1 = game(board)
    assert game1.gameboard() == board.board()
    game1.move_an_o(1, 0, 0, 1, 0)
    board2 = [
        [' ', 'O', ' ', 'x', ' ', 'x', ' ', 'x'],
        [' ', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
        [' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o'],
        ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
    ]
    assert game1.gameboard() == board2


def test_bad_move_an_o():
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
    board = game_board(board2)
    game1 = game(board)
    assert game1.gameboard() == board.board()
    with pytest.raises(PawnMovingBackwardsError):
        game1.move_an_o(4, 1, 5, 0, 0)


def test_standard_move_an_x():
    board = game_board()
    game1 = game(board)
    assert game1.gameboard() == board.board()
    game1.move_an_x(2, 1, 3, 0, 0)
    board2 = [
        [' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['x', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
        [' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o'],
        ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
    ]
    assert game1.gameboard() == board2


def test_move_an_x_to_king():
    board1 = [
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['o', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
        [' ', 'x', ' ', 'o', ' ', 'o', ' ', 'o'],
        [' ', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
    ]
    board = game_board(board1)
    game1 = game(board)
    assert game1.gameboard() == board.board()
    game1.move_an_x(6, 1, 7, 0, 0)
    board2 = [
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['o', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
        [' ', ' ', ' ', 'o', ' ', 'o', ' ', 'o'],
        ['X', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
    ]
    assert game1.gameboard() == board2


def test_bad_move_an_x():
    board2 = [
        [' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['x', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
        [' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o'],
        ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
    ]
    board = game_board(board2)
    game1 = game(board)
    assert game1.gameboard() == board.board()
    with pytest.raises(PawnMovingBackwardsError):
        game1.move_an_x(3, 0, 2, 1, 0)


def test_remove_captured_piece():
    board1 = [
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['o', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
        [' ', 'x', ' ', 'o', ' ', 'o', ' ', 'o'],
        [' ', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
    ]
    board = game_board(board1)
    game1 = game(board)
    assert game1.gameboard() == board.board()
    game1.remove_captured_piece(7, 2, 5, 0)
    board2 = [
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['o', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
        [' ', ' ', ' ', 'o', ' ', 'o', ' ', 'o'],
        [' ', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
    ]
    assert game1.gameboard() == board2


def test_bad_remove_captured_piece():
    board2 = [
        [' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['x', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
        [' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o'],
        ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
    ]
    board = game_board(board2)
    game1 = game(board)
    assert game1.gameboard() == board.board()
    with pytest.raises(CapturingNothingError):
        game1.remove_captured_piece(5, 0, 3, 2)


def test_bad_remove_captured_piece2():
    board2 = [
        [' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['x', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
        [' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o'],
        ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
    ]
    board = game_board(board2)
    game1 = game(board)
    assert game1.gameboard() == board.board()
    with pytest.raises(CapturingYourOwnPiceError):
        game1.remove_captured_piece(6, 1, 4, 3)


def test_PUSH_or_capture_o():
    board = game_board()
    game1 = game(board)
    assert game1.gameboard() == board.board()
    move = push((5, 0), (4, 1))
    game1.push_or_capture(move, 0)
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


def test_push_or_CAPTURE_o():
    board1 = [
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['o', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
        [' ', 'x', ' ', 'o', ' ', 'o', ' ', 'o'],
        [' ', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
    ]
    board = game_board(board1)
    game1 = game(board)
    assert game1.gameboard() == board.board()
    move = capture((7, 2), (5, 0))
    game1.push_or_capture(move, 1)
    board2 = [
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['o', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
        [' ', ' ', ' ', 'o', ' ', 'o', ' ', 'o'],
        [' ', ' ', ' ', ' ', 'o', ' ', 'o', ' '],
    ]
    assert game1.gameboard() == board2


def test_PUSH_or_capture_x():
    board = game_board()
    game1 = game(board)
    assert game1.gameboard() == board.board()
    move = push((2, 1), (3, 0))
    game1.push_or_capture(move, 0)
    board2 = [
        [' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['x', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
        [' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o'],
        ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
    ]
    assert game1.gameboard() == board2


def test_push_or_CAPTURE_x():
    board1 = [
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        [' ', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', 'o', ' ', 'x', ' ', 'x', ' ', 'x'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
        [' ', 'x', ' ', 'o', ' ', 'o', ' ', 'o'],
        [' ', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
    ]
    board = game_board(board1)
    game1 = game(board)
    assert game1.gameboard() == board.board()
    move = capture((1, 2), (3, 0))
    game1.push_or_capture(move, 1)
    board2 = [
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        [' ', ' ', ' ', ' ', 'x', ' ', 'x', ' '],
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
        [' ', 'x', ' ', 'o', ' ', 'o', ' ', 'o'],
        [' ', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
    ]
    assert game1.gameboard() == board2


def test_push_or_capture_king():
    board1 = [
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['o', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
        [' ', 'x', ' ', 'o', ' ', 'o', ' ', 'o'],
        [' ', ' ', 'O', ' ', 'o', ' ', 'o', ' '],
    ]
    board = game_board(board1)
    game1 = game(board)
    assert game1.gameboard() == board.board()
    move = capture((7, 2), (5, 0))
    game1.push_or_capture(move, 1)
    board2 = [
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['o', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['O', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
        [' ', ' ', ' ', 'o', ' ', 'o', ' ', 'o'],
        [' ', ' ', ' ', ' ', 'o', ' ', 'o', ' '],
    ]
    assert game1.gameboard() == board2


def test_bad_push_or_capture():
    board = game_board()
    game1 = game(board)
    assert game1.gameboard() == board.board()
    move = push((4, 1), (3, 2))
    with pytest.raises(NoPieceOnTheSquareError):
        game1.push_or_capture(move, 0)


def test_make_a_move_push():
    board = game_board()
    game1 = game(board)
    assert game1.gameboard() == board.board()
    move = push((5, 0), (4, 1))
    game1.make_a_move(move)
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


def test_make_a_move_capture():
    board1 = [
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['o', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
        [' ', 'x', ' ', 'o', ' ', 'o', ' ', 'o'],
        [' ', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
    ]
    board = game_board(board1)
    game1 = game(board)
    assert game1.gameboard() == board.board()
    move = capture((7, 2), (5, 0))
    game1.make_a_move(move)
    board2 = [
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['o', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
        [' ', ' ', ' ', 'o', ' ', 'o', ' ', 'o'],
        [' ', ' ', ' ', ' ', 'o', ' ', 'o', ' '],
    ]
    assert game1.gameboard() == board2


def test_bad_make_a_move():
    board = game_board()
    game1 = game(board)
    assert game1.gameboard() == board.board()
    with pytest.raises(NotAMoveError):
        game1.make_a_move('move')


def test_check_for_captures_TRUE():
    board1 = [
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['o', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
        [' ', 'x', ' ', 'o', ' ', 'o', ' ', 'o'],
        [' ', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
    ]
    board = game_board(board1)
    game1 = game(board)
    assert game1.gameboard() == board.board()
    assert game1.check_for_captures(1) == 1


def test_check_for_captures_FALSE():
    board1 = [
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['o', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
        [' ', 'x', ' ', 'o', ' ', 'o', ' ', 'o'],
        [' ', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
    ]
    board = game_board(board1)
    game1 = game(board)
    assert game1.gameboard() == board.board()
    assert game1.check_for_captures(0) == 0
