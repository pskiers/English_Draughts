from game_board import game_board
from Errors import (
    SquareTakenError,
    NoPieceOnTheSquareError,
    CapturingNothingError,
    CapturingYourOwnPiceError,
    NotAMoveError,
    PawnMovingBackwardsError,
)


class game:
    """
    """
    def __init__(self, board: 'game_board'):
        self._gameboard = board.board()

    def gameboard(self):
        return self._gameboard

    def make_a_move(self, move):
        if type(move).__name__ == 'push':
            self.push_or_capture(move, 0)
        elif type(move).__name__ == 'capture':
            self.push_or_capture(move, 1)
        else:
            raise NotAMoveError()

    def remove_captured_piece(self, x1, y1, x2, y2):
        rmx = int((x2 + x1) / 2)
        rmy = int((y2 + y1) / 2)
        captured = self.gameboard()[rmx][rmy]
        if captured == ' ':
            raise CapturingNothingError()
        elif captured == self.gameboard()[x1][y1]:
            raise CapturingYourOwnPiceError()
        else:
            self.gameboard()[rmx][rmy] = ' '

    def push_or_capture(self, move, op: bool):
        x1, y1 = move.origin()
        x2, y2 = move.destination()
        if op == 1:
            self.remove_captured_piece(x1, y1, x2, y2)
        if self.gameboard()[x1][y1] == 'o':
            self.move_an_o(x1, y1, x2, y2)
        elif self.gameboard()[x1][y1] == 'x':
            self.move_an_x(x1, y1, x2, y2)
        elif self.gameboard()[x1][y1] == ' ':
            raise NoPieceOnTheSquareError()
        else:
            self.just_move(x1, y1, x2, y2)

    def just_move(self, x1, y1, x2, y2):
        if self.gameboard()[x2][y2] == ' ':
            self.gameboard()[x2][y2] = self.gameboard()[x1][y1]
            self.gameboard()[x1][y1] = ' '
        else:
            raise SquareTakenError()

    def move_an_o(self, x1, y1, x2, y2):
        if x1 < x2:
            raise PawnMovingBackwardsError()
        else:
            if x2 == 0:
                self.gameboard()[x1][y1] = 'O'
            self.just_move(x1, y1, x2, y2)

    def move_an_x(self, x1, y1, x2, y2):
        if x1 > x2:
            raise PawnMovingBackwardsError()
        else:
            if x2 == 7:
                self.gameboard()[x1][y1] = 'X'
            self.just_move(x1, y1, x2, y2)
