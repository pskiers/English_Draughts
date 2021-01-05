import pytest
from moves import push, capture
from Errors import (
    BoardRowCountError,
    RowLengthError,
    PieceOnAWhiteSquareError,
    NotAllowedThingOnTheBoardError,
    NonIterableRowError,
    NonIterableBoardError,
    PawnMovingBackwardsError,
    SquareTakenError,
    CapturingNothingError,
    CapturingYourOwnPiceError,
    NoPieceOnTheSquareError,
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
    with pytest.raises(SquareTakenError):
        board.just_move(6, 1, 5, 0, 0)


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
    with pytest.raises(PawnMovingBackwardsError):
        board.move_an_o(4, 1, 5, 0, 0)


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
    with pytest.raises(PawnMovingBackwardsError):
        board.move_an_x(3, 0, 2, 1, 0)


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
    with pytest.raises(CapturingNothingError):
        board.remove_captured_piece(5, 0, 3, 2)


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
    with pytest.raises(CapturingYourOwnPiceError):
        board.remove_captured_piece(6, 1, 4, 3)


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
    with pytest.raises(NoPieceOnTheSquareError):
        board.push_or_capture(move, 0)


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
