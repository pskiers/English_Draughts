from game import game
from players import Player
from game_board import game_board


def main():
    board = game_board()
    new_game = game(board)
    player0 = Player('carlsen', 0)
    player1 = Player('nakamura', 1)
    new_game.play(player0, player1)


main()
