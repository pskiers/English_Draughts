from Errors import InvalidNameError
from game_board import game_board
from algorithm import algorithm
from cool_interfce import get_coordinates_from_mouse
import pygame


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
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                else:
                    if self.ai() == 0:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos = pygame.mouse.get_pos()
                            x1, y1 = get_coordinates_from_mouse(pos)
                            x2, y2 = get_destination()
                            return x1, y1, x2, y2
                    else:
                        return algorithm(gameboard, turn, 3)


def get_destination():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x2, y2 = get_coordinates_from_mouse(pos)
                return x2, y2
