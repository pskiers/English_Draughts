from Errors import (
    BoardRowCountError,
    RowLengthError,
    PieceOnAWhiteSquareError,
    NotAllowedThingOnTheBoardError,
    NonIterableRowError,
    NonIterableBoardError,
    SquareTakenError,
    NoPieceOnTheSquareError,
    CapturingNothingError,
    CapturingYourOwnPiceError,
    NotAMoveError,
    PawnMovingBackwardsError,
)
from moves import push, capture


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

    def make_a_move(self, move):
        """
        make_a_move method makes a move on the game's gameboard

        :param move: move that is to be made
        :param type: class push or class capture
        """
        if type(move).__name__ == 'push':
            self.push_or_capture(move, 0)
        elif type(move).__name__ == 'capture':
            self.push_or_capture(move, 1)
        else:
            raise NotAMoveError()

    def remove_captured_piece(self, x1, y1, x2, y2):
        """
        remove_captured_piece method removes captured piece from the board
        :param x1: starting row of the capturing piece
        :param type: int
        :param y1: starting column of the capturing piece
        :param type: int
        :param x2: destination row of the capturing piece
        :param type: int
        :param y2: destination column of the capturing piece
        :param type: int
        """
        rmx = int((x2 + x1) / 2)
        rmy = int((y2 + y1) / 2)
        captured = self.board()[rmx][rmy]
        if captured == ' ':
            raise CapturingNothingError()
        elif captured.lower() == self.board()[x1][y1].lower():
            raise CapturingYourOwnPiceError()
        else:
            self.board()[rmx][rmy] = ' '

    def push_or_capture(self, move, op: bool):
        """
        push_or_capture method identifies which function should be used to
        make the move

        :param move: move to be made
        :param type: class push or capture
        :param op: indicates whether move is a capture move
        :param op: bool
        """
        x1, y1 = move.origin()
        x2, y2 = move.destination()
        if self.board()[x1][y1] == 'o':
            self.move_an_o(x1, y1, x2, y2, op)
        elif self.board()[x1][y1] == 'x':
            self.move_an_x(x1, y1, x2, y2, op)
        elif self.board()[x1][y1] == ' ':
            raise NoPieceOnTheSquareError()
        else:
            self.just_move(x1, y1, x2, y2, op)

    def just_move(self, x1, y1, x2, y2, op: bool):
        """
        just_move method simply makes a move

        :param x1: starting row of the moving piece
        :param type: int
        :param y1: starting column of the moving piece
        :param type: int
        :param x2: destination row of the moving piece
        :param type: int
        :param y2: destination column of the moving piece
        :param type: int
        :param op: indicates whether move is a capture move
        :param op: bool
        """
        if self.board()[x2][y2] == ' ':
            if op == 1:
                self.remove_captured_piece(x1, y1, x2, y2)
            self.board()[x2][y2] = self.board()[x1][y1]
            self.board()[x1][y1] = ' '
        else:
            raise SquareTakenError()

    def move_an_o(self, x1, y1, x2, y2, op: bool):
        """
        move_an_o method moves 'o' type pieces

        :param x1: starting row of the moving piece
        :param type: int
        :param y1: starting column of the moving piece
        :param type: int
        :param x2: destination row of the moving piece
        :param type: int
        :param y2: destination column of the moving piece
        :param type: int
        :param op: indicates whether move is a capture move
        :param op: bool
        """
        if x1 < x2:
            raise PawnMovingBackwardsError()
        else:
            if x2 == 0:
                self.board()[x1][y1] = 'O'
            self.just_move(x1, y1, x2, y2, op)

    def move_an_x(self, x1, y1, x2, y2, op: bool):
        """
        move_an_x method moves 'x' type pieces

        :param x1: starting row of the moving piece
        :param type: int
        :param y1: starting column of the moving piece
        :param type: int
        :param x2: destination row of the moving piece
        :param type: int
        :param y2: destination column of the moving piece
        :param type: int
        :param op: indicates whether move is a capture move
        :param op: bool
        """
        if x1 > x2:
            raise PawnMovingBackwardsError()
        else:
            if x2 == 7:
                self.board()[x1][y1] = 'X'
            self.just_move(x1, y1, x2, y2, op)
