from Errors import (
    BoardRowCountError,
    RowLengthError,
    PieceOnAWhiteSquareError,
    NotAllowedThingOnABoardError,
    NonIterableRowError,
    NonIterableBoardError
)


class game_board:
    """
    Class game_board represents state of the game

    Contains atribute:
    :param board: game board
    :param type: list

    Contains methods:
    board():
        returns value of board atribute
    set_board():
        sets value of board atribute
    """
    def __init__(self, board=None):
        self._board = self.set_board(board)

    def __str__(self):
        return str(self.board())

    def board(self):
        return self._board

    def set_board(self, board):
        if not board:
            self._board = [
                [' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'],
                ['x', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
                [' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
                [' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o'],
                ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
            ]
        else:
            if len(board) != 8:
                raise BoardRowCountError()
            else:
                try:
                    for i in range(1,9):
                        if len(board[i]) != 8:
                            raise RowLengthError()
                        try:
                            for j in range(1, 9):
                                if i % 2 == j % 2:
                                    if board[i][j] != ' ':
                                        raise PieceOnAWhiteSquareError()
                                else:
                                    PosSigns = [' ', 'x', 'X', 'o', 'O']
                                    if board[i][j] not in PosSigns:
                                        raise NotAllowedThingOnABoardError()
                        except TypeError:
                            raise NonIterableRowError()
                except TypeError:
                    raise NonIterableBoardError()
