from game_board import game_board
from moves import capture, push
from players import Player
from turn_changer import change_turn
import pygame
from cool_interfce import draw_board, print_text
from Constants import fps, width, height
from Errors import (
    CoordinatesNotOnTheBoardError,
    ChosenWitheSquareError,
    NotAPushMoveError,
    NotACaptureMoveError,
)


class game:
    """
    Class game represents a game of english draugths.
    Contains attribute:
    :param gameboard: gameboard
    :param board: obj game_board
    """
    def __init__(self, board: 'game_board'):
        self.board = board
        self._gameboard = board.board()

    def gameboard(self):
        return self._gameboard

    def play(self, player0: 'Player', player1: 'Player'):
        """
        play method plays a game

        :param player0: 'o' pieces player
        :param type: class Player
        :param player1: 'x' pieces player
        :param type: class Player
        """
        # declaring some variables
        turn = 1
        pieces = [
            ['o', 'O'],
            ['x', 'X'],
        ]
        names = [player0.name, player1.name]
        moves_to_draw = 30
        # initiating pygame
        pygame.init()
        WIN = pygame.display.set_mode((width, height))
        pygame.display.set_caption('English Graughts')
        clock = pygame.time.Clock()
        # game loop
        while True:
            clock.tick(fps)
            draw_board(self.board, WIN)
            # if there has been 30 moves without a change in amount of
            # non-king pieces game ends in a draw
            if moves_to_draw == 0:
                print_text('Game ended in a draw', WIN, pause=1)
                break
            # if it is possible to capture a piece
            if self.board.can_make_a_move(turn, capt=1):
                text = f"It is {names[turn]}'s turn"
                # display text in window
                print_text(text, WIN)
                if turn == 0:
                    t = turn
                    # get move from the player
                    x1, y1, x2, y2, run = player0.get_move(self.board, t, WIN)
                    # if player closed window
                    if not run:
                        break
                else:
                    t = turn
                    # get move from the player
                    x1, y1, x2, y2, run = player1.get_move(self.board, t, WIN)
                    # if player closed window
                    if not run:
                        break
                # trying to make a move
                try:
                    move = capture((x1, y1), (x2, y2))
                    # reseting amount of moves to draw
                    moves_to_draw = 30
                # if some thing goes wrong
                except CoordinatesNotOnTheBoardError:
                    msg = 'Please enter coordinates that are on the board'
                    print_text(msg, WIN, pause=1)
                    continue
                except ChosenWitheSquareError:
                    msg = 'Coordinates cannot point on a white sqare'
                    print_text(msg, WIN, pause=1)
                    continue
                except NotACaptureMoveError:
                    msg = 'You must make a capture move, if you can'
                    print_text(msg, WIN, pause=1)
                    continue
                except (TypeError, ValueError):
                    print_text('Enter some real coordinates', WIN, pause=1)
                    continue
            else:
                # if player can make no move at all
                if not self.board.can_make_a_move(turn, capt=0):
                    # the player on the move has lost, ending the game
                    print_text(f'{names[turn]} has lost', WIN, 1)
                    break
                print_text(f"It is {names[turn]}'s turn", WIN)
                if turn == 0:
                    t = turn
                    # get move from the player
                    x1, y1, x2, y2, run = player0.get_move(self.board, t, WIN)
                    # if player has closed the window
                    if not run:
                        break
                else:
                    t = turn
                    # get move from the player
                    x1, y1, x2, y2, run = player1.get_move(self.board, t, WIN)
                    # if player has closed the window
                    if not run:
                        break
                # trying to make a move
                try:
                    move = push((x1, y1), (x2, y2))
                    moves_to_draw -= 1
                # if something goes wrong
                except CoordinatesNotOnTheBoardError:
                    msg = 'Please enter coordinates that are on the board'
                    print_text(msg, WIN, pause=1)
                    continue
                except ChosenWitheSquareError:
                    msg = 'Coordinates cannot point to a white sqare'
                    print_text(msg, WIN, pause=1)
                    continue
                except NotAPushMoveError:
                    msg = 'You must make a push since only those are possible'
                    print_text(msg, WIN, pause=1)
                    continue
                except (TypeError, ValueError):
                    print_text('Enter some real coordinates', WIN, pause=1)
                    continue
            promotion = self.board.is_it_a_promotion(x1, y1, x2)
            # if it was a promotion move
            if promotion:
                # reseting amount of moves to draw
                moves_to_draw = 30
            if self.gameboard()[x1][y1] in pieces[turn]:
                print_text('You can only move your own pieces', WIN, 1)
                continue
            # making a move
            msg = self.board.make_a_move(move)
            # if there was an error message
            if msg:
                print_text(msg, WIN, 1)
                continue
            else:
                pass
            # changing turn
            turn = change_turn(turn, self.board, promotion, move)
        pygame.quit()
