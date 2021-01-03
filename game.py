from game_board import game_board
from moves import capture, push
from copy import deepcopy
from players import Player
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
    Class game represents a game of english draugths.
    Contains artibute:
    :param gameboard: gameboard

    Cotains methods:
    maka_a_move:
        makes a move on the gameboard
    check_for_captures:
        checks if there is a capture move on the board
    standard geters and functions auxiliary to method make_a_move
    """
    def __init__(self, board: 'game_board'):
        self.board = board
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
        if self.gameboard()[x1][y1] == 'o':
            self.move_an_o(x1, y1, x2, y2, op)
        elif self.gameboard()[x1][y1] == 'x':
            self.move_an_x(x1, y1, x2, y2, op)
        elif self.gameboard()[x1][y1] == ' ':
            raise NoPieceOnTheSquareError()
        else:
            self.just_move(x1, y1, x2, y2, op)

    def just_move(self, x1, y1, x2, y2, op: bool):
        if self.gameboard()[x2][y2] == ' ':
            if op == 1:
                self.remove_captured_piece(x1, y1, x2, y2)
            self.gameboard()[x2][y2] = self.gameboard()[x1][y1]
            self.gameboard()[x1][y1] = ' '
        else:
            raise SquareTakenError()

    def move_an_o(self, x1, y1, x2, y2, op: bool):
        if x1 < x2:
            raise PawnMovingBackwardsError()
        else:
            if x2 == 0:
                self.gameboard()[x1][y1] = 'O'
            self.just_move(x1, y1, x2, y2, op)

    def move_an_x(self, x1, y1, x2, y2, op: bool):
        if x1 > x2:
            raise PawnMovingBackwardsError()
        else:
            if x2 == 7:
                self.gameboard()[x1][y1] = 'X'
            self.just_move(x1, y1, x2, y2, op)

    def is_it_a_promotion(self, x1, y1, x2):
        if self.gameboard()[x1][y1] == 'x':
            if x2 == 7:
                return True
        elif self.gameboard()[x1][y1] == 'o':
            if x2 == 0:
                return True
        else:
            return False

    def play(self, player0: 'Player', player1: 'Player'):
        turn = 1
        while True:
            print(self.board)
            if self.can_make_a_move(turn, 1):
                if turn == 0:
                    x1, y1, x2, y2 = player0.get_move()
                else:
                    x1, y1, x2, y2 = player1.get_move()
                try:
                    move = capture((x1, y1), (x2, y2))
                except:
                    continue
            else:
                if not self.can_make_a_move(turn, 0):
                    print('Some text informing about who won')
                    break
                if turn == 0:
                    x1, y1, x2, y2 = player0.get_move()
                else:
                    x1, y1, x2, y2 = player1.get_move()
                try:
                    move = push((x1, y1), (x2, y2))
                except:
                    continue
            pormotion = self.is_it_a_promotion(x1, y1, x2)
            try:
                self.make_a_move(move)
            except:
                continue
            if not pormotion:
                if not self.check_if_piece_can_move(x2, y2, 1):
                    turn = (turn + 1) % 2

    def can_make_a_move(self, who: bool, capt: bool):
        if who == 0:
            goodPieces = ['x', 'X']
        else:
            goodPieces = ['o', 'O']
        for i in range(len(self.gameboard())):
            for j in range((i+1) % 2, len(self.gameboard()[i]), 2):
                if self.gameboard()[i][j] in goodPieces:
                    if self.check_if_piece_can_move(i, j, capt):
                        return True
        return False

    def check_if_piece_can_move(self, x, y, capt: bool):
        if capt:
            jump = [-2, 2]
        else:
            jump = [-1, 1]
        test = deepcopy(self)
        for dx in jump:
            for dy in jump:
                try:
                    if capt:
                        move = capture((x, y), (x+dx, y+dy))
                    else:
                        move = push((x, y), (x+dx, y+dy))
                    test.make_a_move(move)
                    return True
                except:
                    continue
        return False


pl0 = Player('adam', 0)
pl1 = Player('bartosz', 0)
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
game1.play(pl0, pl1)
