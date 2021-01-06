from Errors import InvalidNameError
from game_board import game_board
from algorithm import algorithm


class Player():
    """
    Class Player represents a player of a game of english draughts.
    Contains arguments:
    :param name: player's name
    :param type: str
    :param ai: informs whether the player is and AI
    :param type: bool
    """
    def __init__(self, name: str, ai: bool):
        if name.isalpha():
            self.name = name.title()
        else:
            raise InvalidNameError()
        self._ai = ai

    def ai(self):
        return self._ai

    def get_move(self, gameboard: 'game_board', turn):
        """
        get_move method reads coordinates of a move player wants to make
        """
        if self.ai() == 0:
            x1 = int(input('In which row is the piece you want to move '))
            y1 = int(input('In which column is the piece you want to move '))
            x2 = int(input('To which row you want to move the piece '))
            y2 = int(input('To which column you want to move the piece '))
            return x1, y1, x2, y2
        else:
            return algorithm(gameboard, turn, 5)
