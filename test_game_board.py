import pytest
from moves import push, capture
from Errors import (
    BoardRowCountError,
    RowLengthError,
    PieceOnAWhiteSquareError,
    NotAllowedThingOnTheBoardError,
    NonIterableRowError,
    NonIterableBoardError,
    NotAMoveError,
)
from game_board import game_board


def test_createDefaultGameBoard():
    board = game_board()
    standardboard = [
        [' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['x', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
        [' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o'],
        ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
    ]
    assert board.board() == standardboard


def test_createGameBoard():
    board = [
        [' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['x', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        [' ', ' ', 'x', ' ', ' ', ' ', ' ', ' '],
        [' ', 'o', ' ', ' ', ' ', ' ', ' ', ' '],
        ['o', ' ', ' ', ' ', 'o', ' ', 'o', ' '],
        [' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o'],
        ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
    ]
    somegame = game_board(board)
    assert somegame.board() == board


def test_createBadGameBoard():
    board = [
        [' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['x', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        [' ', ' ', 'x', ' ', ' ', ' ', ' ', ' '],
        [' ', 'o', ' ', ' ', ' ', ' ', ' ', ' '],
        ['o', ' ', ' ', ' ', 'o', ' ', 'o', ' '],
        [' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o'],
    ]
    with pytest.raises(BoardRowCountError):
        game_board(board)


def test_createBadGameBoard2():
    board = [
        [' ', 'x', ' ', 'x', ' ', 'x', ' '],
        ['x', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        [' ', ' ', 'x', ' ', ' ', ' ', ' ', ' '],
        [' ', 'o', ' ', ' ', ' ', ' ', ' ', ' '],
        ['o', ' ', ' ', ' ', 'o', ' ', 'o', ' '],
        [' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o'],
        ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
    ]
    with pytest.raises(RowLengthError):
        game_board(board)


def test_createBadGameBoard3():
    board = [
        [' ', 'x', ' ', 'x', ' ', 'x', 'x', 'x'],
        ['x', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        [' ', ' ', 'x', ' ', ' ', ' ', ' ', ' '],
        [' ', 'o', ' ', ' ', ' ', ' ', ' ', ' '],
        ['o', ' ', ' ', ' ', 'o', ' ', 'o', ' '],
        [' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o'],
        ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
    ]
    with pytest.raises(PieceOnAWhiteSquareError):
        game_board(board)


def test_createBadGameBoard4():
    board = [
        [' ', 'x', ' ', 'x', ' ', '1', ' ', 'x'],
        ['x', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        [' ', ' ', 'x', ' ', ' ', ' ', ' ', ' '],
        [' ', 'o', ' ', ' ', ' ', ' ', ' ', ' '],
        ['o', ' ', ' ', ' ', 'o', ' ', 'o', ' '],
        [' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o'],
        ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
    ]
    with pytest.raises(NotAllowedThingOnTheBoardError):
        game_board(board)


def test_createBadGameBoard5():
    board = 2
    with pytest.raises(NonIterableBoardError):
        game_board(board)


def test_createBadGameBoard6():
    board = [
        1,
        ['x', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        [' ', ' ', 'x', ' ', ' ', ' ', ' ', ' '],
        [' ', 'o', ' ', ' ', ' ', ' ', ' ', ' '],
        ['o', ' ', ' ', ' ', 'o', ' ', 'o', ' '],
        [' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o'],
        ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
    ]
    with pytest.raises(NonIterableRowError):
        game_board(board)


def test_just_move():
    board = game_board()
    board.just_move(5, 0, 4, 1, 0)
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
    assert board.board() == board2


def test_just_bad_move():
    board = game_board()
    assert board.just_move(6, 1, 5, 0, 0) == 'This square is already taken'


def test_standard_move_an_o():
    board = game_board()
    board.move_an_o(5, 0, 4, 1, 0)
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
    assert board.board() == board2


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
    board.move_an_o(1, 0, 0, 1, 0)
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
    assert board.board() == board2


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
    assert board.move_an_o(4, 1, 5, 0, 0) == 'You cannot move backwards'


def test_standard_move_an_x():
    board = game_board()
    board.move_an_x(2, 1, 3, 0, 0)
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
    assert board.board() == board2


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
    board.move_an_x(6, 1, 7, 0, 0)
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
    assert board.board() == board2


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
    assert board.move_an_x(3, 0, 2, 1, 0) == 'You cannot move backwards'


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
    board.remove_captured_piece(7, 2, 5, 0)
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
    assert board.board() == board2


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
    msg = 'You cannot capture nothing'
    assert board.remove_captured_piece(5, 0, 3, 2) == msg


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
    msg = 'You cannot capture your own piece'
    assert board.remove_captured_piece(6, 1, 4, 3) == msg


def test_PUSH_or_capture_o():
    board = game_board()
    move = push((5, 0), (4, 1))
    board.push_or_capture(move, 0)
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
    assert board.board() == board2


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
    move = capture((7, 2), (5, 0))
    board.push_or_capture(move, 1)
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
    assert board.board() == board2


def test_PUSH_or_capture_x():
    board = game_board()
    move = push((2, 1), (3, 0))
    board.push_or_capture(move, 0)
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
    assert board.board() == board2


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
    move = capture((1, 2), (3, 0))
    board.push_or_capture(move, 1)
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
    assert board.board() == board2


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
    move = capture((7, 2), (5, 0))
    board.push_or_capture(move, 1)
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
    assert board.board() == board2


def test_bad_push_or_capture():
    board = game_board()
    move = push((4, 1), (3, 2))
    assert board.push_or_capture(move, 0) == 'There is no piece on this square'


def test_make_a_move_push():
    board = game_board()
    move = push((5, 0), (4, 1))
    board.make_a_move(move)
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
    assert board.board() == board2


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
    move = capture((7, 2), (5, 0))
    board.make_a_move(move)
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
    assert board.board() == board2


def test_bad_make_a_move():
    board = game_board()
    with pytest.raises(NotAMoveError):
        board.make_a_move('move')


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
    assert board.can_make_a_move(1, 1) == 1


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
    assert board.can_make_a_move(0, 1) == 0


def test_check_for_pushes_TRUE():
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
    assert board.can_make_a_move(0, 0) == 1


def test_check_for_pushes_FALSE():
    board1 = [
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['o', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', 'o', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
        [' ', 'o', ' ', 'o', ' ', 'o', ' ', ' '],
        [' ', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
        [' ', 'x', ' ', 'o', ' ', 'o', ' ', 'o'],
        ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
    ]
    board = game_board(board1)
    assert board.can_make_a_move(0, 0) == 0


def test_check_if_piece_can_move_Capt_TRUE():
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
    assert board.check_if_piece_can_move(7, 2, 1) == 1


def test_check_if_piece_can_move_Capt_FALSE():
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
    assert board.check_if_piece_can_move(5, 2, 1) == 0


def test_check_if_piece_can_move_Push_FALSE():
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
    assert board.check_if_piece_can_move(7, 2, 0) == 0


def test_check_if_piece_can_move_Push_TRUE():
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
    assert board.check_if_piece_can_move(5, 2, 0) == 1


def test_is_it_a_promotion_o_TRUE():
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
    assert board.is_it_a_promotion(1, 0, 0) == 1


def test_is_it_a_promotion_x_TRUE():
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
    assert board.is_it_a_promotion(6, 1, 7) == 1


def test_is_it_a_promotion_FALSE_alreadyKing():
    board1 = [
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['O', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
        [' ', 'x', ' ', 'o', ' ', 'o', ' ', 'o'],
        [' ', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
    ]
    board = game_board(board1)
    assert board.is_it_a_promotion(1, 0, 0) == 0


def test_is_it_a_promotion_justFALSE():
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
    assert board.is_it_a_promotion(5, 2, 4) == 0


def test_is_this_move_legal_capture_TRUE():
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
    assert board.is_this_move_legal(7, 2, -2, -2, 1) == 1


def test_is_this_move_legal_capture_FALSE():
    board1 = [
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        ['o', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
        [' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['x', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
        [' ', 'x', ' ', 'o', ' ', 'o', ' ', 'o'],
        [' ', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
    ]
    board = game_board(board1)
    assert board.is_this_move_legal(7, 2, -2, -2, 1) == 0


def test_is_this_move_legal_push_TRUE():
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
    assert board.is_this_move_legal(5, 2, -1, -1, 0) == 1


def test_is_this_move_legal_push_FALSE():
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
    assert board.is_this_move_legal(7, 2, -1, -1, 0) == 0
