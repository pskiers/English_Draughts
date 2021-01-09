from game_board import game_board
from moves import capture, push
from players import Player
from turn_changer import change_turn
import pygame
from cool_interfce import draw_board
from Constants import fps, width, height
from Errors import (
    SquareTakenError,
    NoPieceOnTheSquareError,
    CapturingNothingError,
    CapturingYourOwnPiceError,
    PawnMovingBackwardsError,
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
        :param player1: 'x: pieces player
        :param type: class Player
        """
        turn = 1
        pieces = [
            ['o', 'O'],
            ['x', 'X'],
        ]
        names = [player0.name, player1.name]
        moves_to_draw = 30
        pygame.init()
        WIN = pygame.display.set_mode((width, height))
        pygame.display.set_caption('English Graughts')
        clock = pygame.time.Clock()
        while True:
            clock.tick(fps)
            draw_board(self.board, WIN)
            if moves_to_draw == 0:
                print('Game ended in a draw')
                break
            if self.board.can_make_a_move(turn, 1):
                print(f"It is {names[turn]}'s turn")
                if turn == 0:
                    try:
                        t = turn
                        x1, y1, x2, y2 = player0.get_move(self.board, t, WIN)
                    except Exception:
                        print('Please enter real coordinates')
                        continue
                else:
                    try:
                        t = turn
                        x1, y1, x2, y2 = player1.get_move(self.board, t, WIN)
                    except Exception:
                        print('Please enter real coordinates')
                        continue
                try:
                    move = capture((x1, y1), (x2, y2))
                    moves_to_draw = 30
                except CoordinatesNotOnTheBoardError:
                    print('Please enter coordinates that are on the board')
                    continue
                except ChosenWitheSquareError:
                    print('Coordinates cannot point on a white sqare')
                    continue
                except NotACaptureMoveError:
                    print('You must make a capture move, if you can')
                    continue
                except (TypeError, ValueError):
                    print('Please enter some real coordinates')
                    continue
            else:
                if not self.board.can_make_a_move(turn, 0):
                    print(f'{names[turn]} has lost')
                    break
                print(f"It is {names[turn]}'s turn")
                if turn == 0:
                    try:
                        t = turn
                        x1, y1, x2, y2 = player0.get_move(self.board, t, WIN)
                    except Exception:
                        print('Please enter real coordinates')
                        continue
                else:
                    try:
                        t = turn
                        x1, y1, x2, y2 = player1.get_move(self.board, t, WIN)
                    except Exception:
                        print('Please enter real coordinates')
                        continue
                try:
                    move = push((x1, y1), (x2, y2))
                    moves_to_draw -= 1
                except CoordinatesNotOnTheBoardError:
                    print('Please enter coordinates that are on the board')
                    continue
                except ChosenWitheSquareError:
                    print('Coordinates cannot point to a white sqare')
                    continue
                except NotAPushMoveError:
                    print('You must make a push since only those are possible')
                    continue
                except (TypeError, ValueError):
                    print('Please enter some real coordinates')
                    continue
            promotion = self.board.is_it_a_promotion(x1, y1, x2)
            if promotion:
                moves_to_draw = 30
            if self.gameboard()[x1][y1] in pieces[turn]:
                print('You can only move your own pieces')
                continue
            try:
                self.board.make_a_move(move)
            except SquareTakenError:
                print('You cannot move to a sqare that is already taken')
                continue
            except NoPieceOnTheSquareError:
                print('You cannot move nothing')
                continue
            except CapturingNothingError:
                print('You cannot capture nothing')
                continue
            except CapturingYourOwnPiceError:
                print('You cannot capture your own piece')
                continue
            except PawnMovingBackwardsError:
                print('You cannot move backwards')
                continue
            turn = change_turn(turn, self.board, promotion, move)
        pygame.quit()
