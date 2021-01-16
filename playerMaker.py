from players import Player
from Errors import InvalidNameError


def create_2_players():
    """
    Creates a 2 players
    """
    print('Create first player')
    player1 = create_player()
    print('Create second player')
    player2 = create_player()
    return player1, player2


def create_player():
    """
    Creates 1 player
    """
    while True:
        ai = get_ai()
        if ai is None:
            continue
        else:
            pass
        name = input('What is this player name? ')
        try:
            player = Player(name, ai)
            return player
        except InvalidNameError:
            print('That is not a name')


def get_ai():
    ai = input('Is this an ai? ')
    if ai.lower() == 'no':
        return 0
    elif ai.lower() == 'yes':
        return 1
    else:
        print("I don't understand")
        return None
