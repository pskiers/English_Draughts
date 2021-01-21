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
    if not board.can_make_a_move(turn, capt=1):
        if not board.can_make_a_move(turn, 0):
            # player cannot make a move so he lost
            return 1000000 * (1 - (turn * 2))
    for x in range(len(board.board())):
        for y in range((x+1) % 2, len(board.board()[x]), 2):
            square = board.board()[x][y]
            # estimating and adding value of piece to estimation
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
    # checking for any captures
    capt = board.can_make_a_move(turn, 1)
    # for every black square
    for i in range(len(board.board())):
        for j in range((i+1) % 2, len(board.board()[i]), 2):
            # if piece belongs to player on the move
            if board.board()[i][j] in pieces[turn]:
                # for every potentially legal move
                for dx in jump[capt]:
                    for dy in jump[capt]:
                        # if jump lands on the board
                        if i+dx in range(8) and j+dy in range(8):
                            if board.is_this_move_legal(i, j, dx, dy, capt):
                                if capt:
                                    move = capture((i, j), (i+dx, j+dy))
                                else:
                                    move = push((i, j), (i+dx, j+dy))
                                all_the_right_moves.append(move)
                        else:
                            pass
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
        # if depth is 0 or node is terminal
        return evaluate(board, turn)
    if turn:
        # minus infinity equivalent
        value = -1000000
        moves = get_all_moves(board, turn)
        # for each child of the node
        for move in moves:
            x1, y1 = move.origin()
            x2, y2 = move.destination()
            # creating a "child" board
            new_board = deepcopy(board)
            prom = new_board.is_it_a_promotion(x1, y1, x2)
            new_board.make_a_move(move)
            # calculating new turn value
            new_t = change_turn(turn, new_board, prom, move)
            value = max(value, alp_bet(new_board, new_t, depth-1, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                # beta cutoff
                break
        return value
    else:
        # plus infinity equivalent
        value = 1000000
        moves = get_all_moves(board, turn)
        # for each child of the node
        for move in moves:
            x1, y1 = move.origin()
            x2, y2 = move.destination()
            # creating a "child" board
            new_board = deepcopy(board)
            prom = new_board.is_it_a_promotion(x1, y1, x2)
            new_board.make_a_move(move)
            # calculating new turn value
            new_t = change_turn(turn, new_board, prom, move)
            value = min(value, alp_bet(new_board, new_t, depth-1, alpha, beta))
            beta = min(beta, value)
            if beta <= alpha:
                # alpha cutoff
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
        # creating new board for situation after the move
        new_board = deepcopy(board)
        prom = new_board.is_it_a_promotion(x1, y1, x2)
        new_board.make_a_move(move)
        # calculating new turn
        new_t = change_turn(turn, new_board, prom, move)
        if turn:
            # if after the move board has better evaluation than the current
            # best
            if alp_bet(new_board, new_t, depth-1) > best_evaluation:
                best_evaluation = alp_bet(new_board, new_t, depth-1)
                best_move = move
        else:
            # if after this move board has better evaluation than the current
            # best
            if alp_bet(new_board, new_t, depth-1) < best_evaluation:
                best_evaluation = alp_bet(new_board, new_t, depth-1)
                best_move = move
    x1, y1 = best_move.origin()
    x2, y2 = best_move.destination()
    return x1, y1, x2, y2
