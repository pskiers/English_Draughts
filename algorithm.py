from game_board import game_board
from moves import push, capture


def evaluate(board: 'game_board', turn):
    """
    Function evaluate evaluates current position. The bigger the
    evaluation the better for 'o' player and worse for the 'x' player.
    1000 = 'o' player won, -1000 = 'x' player won

    :param board: current state of the game on the board
    :param type: game_board
    :param turn: is 'o' (1) on the move or 'x' (0)
    :param type: bool
    """
    estimation = 0
    if not board.can_make_a_move(turn, 1):
        if not board.can_make_a_move(turn, 0):
            return 1000 * (1 - (turn * 2))
    for x in range(len(board.board())):
        for y in range((x+1) % 2, len(board.board()[x]), 2):
            square = board.board()[x][y]
            if square == 'X':
                estimation -= 20
                pos_value = 0
                if x == 7 or x == 0:
                    pos_value -= 1
                if y == 0 or y == 7:
                    pos_value -= 1
                estimation += pos_value
            elif square == 'O':
                estimation += 20
                pos_value = 0
                if x == 7 or x == 0:
                    pos_value += 1
                if y == 0 or y == 7:
                    pos_value += 1
                estimation += pos_value
            elif square == 'x':
                estimation -= 10
                pos_value = 0
                pos_value -= x
                if y == 0 or y == 7:
                    pos_value -= 1
                estimation += pos_value
            elif square == 'o':
                estimation += 10
                pos_value = 0
                pos_value += (7 - x)
                if y == 0 or y == 7:
                    pos_value += 1
                estimation += pos_value
            else:
                pass
    return estimation


def get_all_moves(board: 'game_board', turn: bool):
    """
    Function returns all legal moves available in the position

    :param board: current position on the board
    :param type: game_board
    :param turn: shows if it is 'o' (1) turn or 'x' (0) turn
    :param type: bool
    """
    all_the_right_moves = []
    pieces = [
        ['x', 'X'],
        ['o', 'O'],
    ]
    jump = [
        [1, -1],
        [2, -2],
    ]
    captures = board.can_make_a_move(turn, 1)

    for i in range(len(board.board())):
        for j in range((i+1) % 2, len(board.board()[i]), 2):
            if board.board()[i][j] in pieces[turn]:
                for dx in jump[captures]:
                    for dy in jump[captures]:
                        if board.is_this_move_legal(i, j, dx, dy, captures):
                            if captures:
                                move = capture((i, j), (i+dx, j+dy))
                            else:
                                move = push((i, j), (i+dx, j+dy))
                            all_the_right_moves.append(move)
    return all_the_right_moves


def alpha_betha(board: 'game_board', turn: bool, depth: int):
    pass
