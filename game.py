from game_board import game_board
from moves import push, capture
from Errors import (
    SquareTakenError,
    NoPieceOnTheSquareError,
    CapturingNothingError,
    CapturingYourOwnPiceError,
)


class game:
    """
    """
    def __init__(self, board: 'game_board'):
        self._gameboard = board.board()

    def gameboard(self):
        return self._gameboard

    def make_a_move(self, move, op: int):
        x1, y1 = move.origin()
        x2, y2 = move.destination()
        pieces = ['x', 'X', 'o', 'O']
        if self.gameboard()[x1][y1] in pieces:
            if self.gameboard()[x2][y2] == ' ':
                if op == 2:
                    captured = self.gameboard()[x2 - 1][y2 - 1]
                    if captured == ' ':
                        raise CapturingNothingError()
                    elif captured == self.gameboard()[x1][y1]:
                        raise CapturingYourOwnPiceError()
                    else:
                        self.gameboard()[x2 - 1][y2 - 1] = ' '
                self.gameboard()[x2][y2] = self.gameboard()[x1][y1]
                self.gameboard()[x1][y1] = ' '
            else:
                raise SquareTakenError()
        else:
            raise NoPieceOnTheSquareError()

    def make_a_push(self, move: 'push'):
        self.make_a_move(move, 1)

    def make_a_capture(self, move: 'capture'):
        self.make_a_move(move, 2)
