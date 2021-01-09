from game import game
from game_board import game_board
from playerMaker import create_2_players


def main():
    board = game_board()
    new_game = game(board)
    player0, player1 = create_2_players()
    new_game.play(player0, player1)


if __name__ == "__main__":
    main()
