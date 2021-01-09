from Errors import InvalidNameError
from game_board import game_board
from algorithm import algorithm
from cool_interfce import get_coordinates_from_mouse
from Constants import sqSize, radiusB, green, black
import pygame
import pygame.gfxdraw


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

    def get_move(self, gameboard: 'game_board', turn, WIN):
        """
        get_move method reads coordinates of a move player wants to make

        :param gameboard: current state of the game on the board
        :param type: game_board
        :param turn: who's turn it is
        :param type: bool
        :param WIN: window where things can be displayed
        :param type: pygame.display
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
                            x = sqSize * x1 + sqSize // 2
                            y = sqSize * y1 + sqSize // 2
                            pygame.gfxdraw.circle(WIN, y, x, radiusB+2, green)
                            pygame.display.update()
                            x2, y2 = get_destination()
                            pygame.gfxdraw.circle(WIN, y, x, radiusB+2, black)
                            pygame.display.update()
                            return x1, y1, x2, y2
                    else:
                        return algorithm(gameboard, turn, 4)


def get_destination():
    """
    Function get_destination returns to which square the player wants to move
    his piece
    """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x2, y2 = get_coordinates_from_mouse(pos)
                return x2, y2
