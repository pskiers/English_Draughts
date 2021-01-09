from game import game
from players import Player
from game_board import game_board


def main():
    board = game_board()
    new_game = game(board)
    player0 = Player('carlsen', 1)
    player1 = Player('nakamura', 0)
    new_game.play(player0, player1)


main()
