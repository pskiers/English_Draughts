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
