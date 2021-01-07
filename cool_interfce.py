import pygame


# some const
red = (255, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
black = (0, 0, 0)
width, height = 800, 800
rowCoun, colCoun = 8, 8
sqSize = width // colCoun
radiusB = sqSize // 2 - 10
radiusS = radiusB - 20


def draw_board(board, WINDOW):
    draw_checkerboard(board, WINDOW)
    draw_pieces(board, WINDOW)
    pygame.display.update()


def draw_checkerboard(board, WINDOW):
    WINDOW.fill(black)
    for row in range(len(board.board())):
        for col in range(row % 2, len(board.board()), 2):
            pygame.draw.rect(WINDOW, white, (row*sqSize, col*sqSize, sqSize, sqSize))


def draw_pieces(board, WINDOW):
    for row in range(len(board.board())):
        for col in range((1+row) % 2, len(board.board()), 2, ):
            sq = board.board()[row][col]
            x = sqSize * col + sqSize // 2
            y = sqSize * row + sqSize // 2
            if sq == 'x':
                pygame.draw.circle(WINDOW, red, (x, y), radiusB)
            elif sq == 'o':
                pygame.draw.circle(WINDOW, white, (x, y), radiusB)
            elif sq == 'X':
                pygame.draw.circle(WINDOW, red, (x, y), radiusB)
                pygame.draw.circle(WINDOW, blue, (x, y), radiusS)
            elif sq == 'O':
                pygame.draw.circle(WINDOW, white, (x, y), radiusB)
                pygame.draw.circle(WINDOW, blue, (x, y), radiusS)
            else:
                pass


def get_coordinates_from_mouse(pos):
    x, y = pos
    row = y // sqSize
    col = x // sqSize
    return row, col
