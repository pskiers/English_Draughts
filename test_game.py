from game import game
from game_board import game_board


def test_createAGame():
    board = game_board()
    game1 = game(board)
    assert game1.gameboard() == board.board()


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
    assert game1.can_make_a_move(1, 1) == 1


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
    assert game1.can_make_a_move(0, 1) == 0


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
    game1 = game(board)
    assert game1.gameboard() == board.board()
    assert game1.can_make_a_move(0, 0) == 1


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
    game1 = game(board)
    assert game1.gameboard() == board.board()
    assert game1.can_make_a_move(0, 0) == 0


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
    game1 = game(board)
    assert game1.gameboard() == board.board()
    assert game1.is_it_a_promotion(1, 0, 0) == 1


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
    game1 = game(board)
    assert game1.gameboard() == board.board()
    assert game1.is_it_a_promotion(6, 1, 7) == 1


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
    game1 = game(board)
    assert game1.gameboard() == board.board()
    assert game1.is_it_a_promotion(1, 0, 0) == 0


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
    game1 = game(board)
    assert game1.gameboard() == board.board()
    assert game1.is_it_a_promotion(5, 2, 4) == 0


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
    game1 = game(board)
    assert game1.gameboard() == board.board()
    assert game1.check_if_piece_can_move(7, 2, 1) == 1


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
    game1 = game(board)
    assert game1.gameboard() == board.board()
    assert game1.check_if_piece_can_move(5, 2, 1) == 0


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
    game1 = game(board)
    assert game1.gameboard() == board.board()
    assert game1.check_if_piece_can_move(7, 2, 0) == 0


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
    game1 = game(board)
    assert game1.gameboard() == board.board()
    assert game1.check_if_piece_can_move(5, 2, 0) == 1
