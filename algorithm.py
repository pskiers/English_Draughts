from game_board import game_board
from moves import push, capture
from copy import deepcopy
from turn_changer import change_turn


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
            return 1000000 * (1 - (turn * 2))
    for x in range(len(board.board())):
        for y in range((x+1) % 2, len(board.board()[x]), 2):
            square = board.board()[x][y]
            if square == 'X':
                estimation -= 40
                pos_value = 0
                if x == 7 or x == 0:
                    pos_value -= 1
                if y == 0 or y == 7:
                    pos_value -= 1
                estimation += pos_value
            elif square == 'O':
                estimation += 40
                pos_value = 0
                if x == 7 or x == 0:
                    pos_value += 1
                if y == 0 or y == 7:
                    pos_value += 1
                estimation += pos_value
            elif square == 'x':
                estimation -= 20
                pos_value = 0
                pos_value -= x
                if y == 0 or y == 7:
                    pos_value -= 1
                estimation += pos_value
            elif square == 'o':
                estimation += 20
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


def alp_bet(board: 'game_board', turn, depth, alpha=-1000000, beta=1000000):
    """
    Function alp_bet is a standard alpha-beta pruning for english draghts

    :param board: current position on the board
    :param type: game_board
    :param turn: is it 'o' turn (1), or 'x' turn (0)
    :param type: bool
    :param depht: how deep shoud the pruning be
    :param type: int
    :param alpha: current alpha value, defaultst to -1000
    :param type: int
    :param beta: current beta value, defaults to 1000
    :param type: int
    """
    if depth == 0 or evaluate(board, turn) in [1000000, -1000000]:
        return evaluate(board, turn)
    if turn:
        value = -1000000
        moves = get_all_moves(board, turn)
        for move in moves:
            x1, y1 = move.origin()
            x2, y2 = move.destination()
            new_board = deepcopy(board)
            prom = new_board.is_it_a_promotion(x1, y1, x2)
            new_board.make_a_move(move)
            new_t = change_turn(turn, new_board, prom, move)
            value = max(value, alp_bet(new_board, new_t, depth-1, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = 1000000
        moves = get_all_moves(board, turn)
        for move in moves:
            x1, y1 = move.origin()
            x2, y2 = move.destination()
            new_board = deepcopy(board)
            prom = new_board.is_it_a_promotion(x1, y1, x2)
            new_board.make_a_move(move)
            new_t = change_turn(turn, new_board, prom, move)
            value = min(value, alp_bet(new_board, new_t, depth-1, alpha, beta))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value


def algorithm(board: 'game_board', turn, depth):
    """
    Algorithm calculates what is the best move in the position looking n move
    forward

    :param board: current position on the board
    :param type: game_board
    :param turn: is it 'o' turn (1), or 'x' turn (0)
    :param type: bool
    :param depht: how deep shoud the pruning be
    :param type: int
    """
    best_move = None
    if turn:
        best_evaluation = -1000001
    else:
        best_evaluation = 1000001
    all_moves = get_all_moves(board, turn)
    for move in all_moves:
        x1, y1 = move.origin()
        x2, y2 = move.destination()
        new_board = deepcopy(board)
        prom = new_board.is_it_a_promotion(x1, y1, x2)
        new_board.make_a_move(move)
        new_t = change_turn(turn, new_board, prom, move)
        if turn:
            if alp_bet(new_board, new_t, depth-1) > best_evaluation:
                best_evaluation = alp_bet(new_board, new_t, depth-1)
                best_move = move
        else:
            if alp_bet(new_board, new_t, depth-1) < best_evaluation:
                best_evaluation = alp_bet(new_board, new_t, depth-1)
                best_move = move
    x1, y1 = best_move.origin()
    x2, y2 = best_move.destination()
    return x1, y1, x2, y2
