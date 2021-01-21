from players import Player
from Errors import InvalidNameError


def create_2_players():
    """
    Creates a 2 players
    """
    print('Create player who goes second')
    player1 = create_player()
    print('Create player who goes first')
    player2 = create_player()
    return player1, player2


def create_player():
    """
    Creates 1 player
    """
    while True:
        ai, depth = get_ai()
        if ai is None:
            continue
        else:
            pass
        name = input("What is this player's name? ")
        try:
            player = Player(name, ai, depth)
            return player
        except InvalidNameError:
            print('That is not a name')


def get_ai():
    ai = input('Is this an ai? ')
    if ai.lower() == 'no':
        return 0, 0
    elif ai.lower() == 'yes':
        depth = get_depth()
        return 1, depth
    else:
        print("I don't understand")
        return None


def get_depth():
    while True:
        depth = input('Choose the depth of the algorithm ')
        try:
            depth = int(depth)
        except ValueError:
            print('Plese enter a number')
            continue
        if depth < 1:
            print('Depth cannot be equal to less than 1')
            continue
        if depth > 6:
            print('Warning: AI might take a long time to make a move')
        return depth
