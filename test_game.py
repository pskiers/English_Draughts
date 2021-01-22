from game import game
from game_board import game_board


def test_createAGame():
    board = game_board()
    game1 = game(board)
    assert game1.gameboard() == board.board()
    assert game1.board == board
