import pygame
import time
from Constants import (
    red, white, blue, black,
    radiusB, radiusS,
    sqSize as sq
)


def draw_board(board, WINDOW):
    """
    Function draw_board draws board on the window

    :param board: board to be drawn
    :param type: game_board
    :param WINDOW: window where the board is suposed to be displayed
    :param type: pygame.display
    """
    draw_checkerboard(board, WINDOW)
    draw_pieces(board, WINDOW)
    pygame.display.update()


def draw_checkerboard(board, WIN):
    """
    Function draw_checkerboard draws checkeboard on the window

    :param board: board
    :param type: game_board
    :param WIN: window where the checkerboard is suposed to be displayed
    :param type: pygame.display
    """
    WIN.fill(black)
    for row in range(len(board.board())):
        for col in range(row % 2, len(board.board()), 2):
            pygame.draw.rect(WIN, white, (row*sq, col*sq, sq, sq))


def draw_pieces(board, WINDOW):
    """
    Function draw_pieces draws pieces from game board on the window

    :param board: gameboard
    :param type: game_board
    :param WINDOW: window where the pieces are suposed to be displayed
    """
    for row in range(len(board.board())):
        for col in range((1+row) % 2, len(board.board()), 2, ):
            csq = board.board()[row][col]
            x = sq * col + sq // 2
            y = sq * row + sq // 2
            if csq == 'x':
                pygame.draw.circle(WINDOW, red, (x, y), radiusB)
            elif csq == 'o':
                pygame.draw.circle(WINDOW, white, (x, y), radiusB)
            elif csq == 'X':
                pygame.draw.circle(WINDOW, red, (x, y), radiusB)
                pygame.draw.circle(WINDOW, blue, (x, y), radiusS)
            elif csq == 'O':
                pygame.draw.circle(WINDOW, white, (x, y), radiusB)
                pygame.draw.circle(WINDOW, blue, (x, y), radiusS)
            else:
                pass


def get_coordinates_from_mouse(pos):
    """
    Function get_coordinates_from_mouse returns coordinates on the gameboard
    from position of the mouse

    :param pos: position of the mouse
    :param type: Tuple(int, int)
    """
    x, y = pos
    row = y // sq
    col = x // sq
    return row, col


def print_text(text, WIN, pause=0):
    newfont = pygame.font.SysFont('text box', 32)
    toblit = newfont.render(text, 0, white, black)
    WIN.blit(toblit, (10, 740))
    pygame.display.update()
    if pause:
        time.sleep(1)
