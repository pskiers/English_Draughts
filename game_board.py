from Errors import (
    BoardRowCountError,
    RowLengthError,
    PieceOnAWhiteSquareError,
    NotAllowedThingOnTheBoardError,
    NonIterableRowError,
    NonIterableBoardError,
    NotAMoveError,
)
from moves import push, capture
from copy import deepcopy


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
        # module for text version of the game and debuging
        # otherwise not very useful
        board = '____________________________________________________\n'
        i = 0
        for row in self.board():
            rowstr = str(i)
            for square in row:
                rowstr += '  |  '
                rowstr += str(square)
            rowstr += '  |\n'
            rowstr += '____________________________________________________\n'
            board += rowstr
            i += 1
        board += '   |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |'
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
            return self.push_or_capture(move, op=0)
        elif type(move).__name__ == 'capture':
            return self.push_or_capture(move, op=1)
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
        # calculating coordinates of captured piece
        rmx = int((x2 + x1) / 2)
        rmy = int((y2 + y1) / 2)
        # captured piece
        captured = self.board()[rmx][rmy]
        if captured == ' ':
            msg = 'You cannot capture nothing'
            return msg
        elif captured.lower() == self.board()[x1][y1].lower():
            msg = 'You cannot capture your own piece'
            return msg
        else:
            # deleting captured piece
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
        # if piece to be moved is an 'o'
        if self.board()[x1][y1] == 'o':
            return self.move_an_o(x1, y1, x2, y2, op)
        # if piece to be moved is an 'x'
        elif self.board()[x1][y1] == 'x':
            return self.move_an_x(x1, y1, x2, y2, op)
        # if there is no piece
        elif self.board()[x1][y1] == ' ':
            msg = 'There is no piece on this square'
            return msg
        else:
            # if the piece is a king
            return self.just_move(x1, y1, x2, y2, op)

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
        # if destination square is empty
        if self.board()[x2][y2] == ' ':
            # if we are capturing
            if op == 1:
                if self.remove_captured_piece(x1, y1, x2, y2):
                    return self.remove_captured_piece(x1, y1, x2, y2)
                else:
                    pass
            # swaping origin of the move with its destination
            self.board()[x2][y2] = self.board()[x1][y1]
            self.board()[x1][y1] = ' '
            # making kings
            if x2 == 0 and self.board()[x2][y2] == 'o':
                self.board()[x2][y2] = 'O'
            if x2 == 7 and self.board()[x2][y2] == 'x':
                self.board()[x2][y2] = 'X'
        # if destination square is not empty
        else:
            msg = 'This square is already taken'
            return msg

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
            msg = 'You cannot move backwards'
            return msg
        else:
            return self.just_move(x1, y1, x2, y2, op)

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
            msg = 'You cannot move backwards'
            return msg
        else:
            return self.just_move(x1, y1, x2, y2, op)

    def can_make_a_move(self, who: bool, capt: bool):
        """
        can_make_a_move method checks if certain player can make a move of
        certain type

        :param who: do we check player0 ('o') (1) or player1 ('x') (0)?
        :param type: bool
        :param capt: do we check for captures (1) or for pushes (0)
        :param type: bool
        """
        # selecting only our player's pieces
        if who == 0:
            goodPieces = ['x', 'X']
        else:
            goodPieces = ['o', 'O']
        # for every black square
        for i in range(len(self.board())):
            for j in range((i+1) % 2, len(self.board()[i]), 2):
                if self.board()[i][j] in goodPieces:
                    if self.check_if_piece_can_move(i, j, capt):
                        return True
        return False

    def check_if_piece_can_move(self, x, y, capt: bool):
        """
        check_if_piece_can_move method checks if certain piece can make
        certain move

        :param x: row in which the piece is
        :param type: int
        :param y: column in which the piece is
        :param type: int
        :param capt: do we check for captures (1) or for pushes (0)
        :param type: bool
        """
        if capt:
            jump = [-2, 2]
        else:
            jump = [-1, 1]
        # for each potentially legal move
        for dx in jump:
            for dy in jump:
                # if jump lands on the board
                if x+dx in range(8) and y+dy in range(8):
                    if self.is_this_move_legal(x, y, dx, dy, capt):
                        return True
                else:
                    pass
        return False

    def is_this_move_legal(self, x, y, dx, dy, capt):
        """
        is_this_move_legal method checks if certain move is legal

        :param x: row in which the piece is
        :param type: int
        :param y: column in which the piece is
        :param type: int
        :param dx: difference in x-coordinate
        :param type: int
        :param dy: difference in y-coordinate
        :param type: int
        :param capt: do we check for captures (1) or for pushes (0)
        :param type: bool
        """
        # creating testing board
        test = deepcopy(self)
        if capt:
            move = capture((x, y), (x+dx, y+dy))
        else:
            move = push((x, y), (x+dx, y+dy))
        if test.make_a_move(move):
            return False
        else:
            return True

    def is_it_a_promotion(self, x1, y1, x2):
        """
        is_it_a_promotion method checks whether the move will result in a
        promotion to king

        :param x1: starting row of the moving piece
        :param type: int
        :param y1: starting column of the moving piece
        :param type: int
        :param x2: destination row of the moving piece
        :param type: int
        """
        if self.board()[x1][y1] == 'x':
            if x2 == 7:
                return True
            else:
                return False
        elif self.board()[x1][y1] == 'o':
            if x2 == 0:
                return True
            else:
                return False
        else:
            return False
