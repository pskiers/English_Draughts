from game_board import game_board


def change_turn(turn: bool, board: 'game_board', promotion: bool, move):
    """
    Based on current turn, game board, move made and promotion status,
    function change_turn determines who's turn it is going to be after
    the move.

    :param turn: determins who's turn it is now
    :param type: bool
    :param board: represents gameboard after move
    :param type: game_board
    :param promotion: indiates if there was a promotion
    :param type: bool
    :param move: move that was just made
    :param type: capture or push
    """
    x2, y2 = move.destination()
    if promotion:
        turn = (turn + 1) % 2
    else:
        if type(move).__name__ == 'capture':
            if not board.check_if_piece_can_move(x2, y2, 1):
                turn = (turn + 1) % 2
        else:
            turn = (turn + 1) % 2
    return turn
