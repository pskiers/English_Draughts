from Errors import (
    BoardRowCountError,
    RowLengthError,
    PieceOnAWhiteSquareError,
    NotAllowedThingOnTheBoardError,
    NonIterableRowError,
    NonIterableBoardError
)


class game_board:
    """
    Class game_board represents state of the game

    Contains attribute:
    :param board: game board
    :param type: list

    Contains methods:
    board():
        returns value of board attribute
    set_board():
        sets value of board attribute
    """
    def __init__(self, board=None):
        self.set_board(board)

    def __str__(self):
        board = ''
        i = 0
        for row in self.board():
            board += str(i)
            board += ' '
            board += str(row)
            board += '\n'
            i += 1
        board += '    0    1    2    3    4    5    6    7  '
        return board

    def board(self):
        return self._board

    def set_board(self, newboard):
        """
        standard setter for board attribute
        """
        if not newboard:
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
            try:
                if len(newboard) != 8:
                    raise BoardRowCountError()
            except TypeError:
                raise NonIterableBoardError()
            else:
                for i in range(8):
                    try:
                        if len(newboard[i]) != 8:
                            raise RowLengthError()
                    except TypeError:
                        raise NonIterableRowError()
                    for j in range(8):
                        if i % 2 == j % 2:
                            if newboard[i][j] != ' ':
                                raise PieceOnAWhiteSquareError()
                        else:
                            PosSigns = [' ', 'x', 'X', 'o', 'O']
                            if newboard[i][j] not in PosSigns:
                                raise NotAllowedThingOnTheBoardError()
                self._board = newboard
