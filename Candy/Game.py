total = 150
game = False


def get_total():
    global total
    return total


def take_candies(take: int):
    global total
    total -= take


def check_game():
    global game
    return game


def new_game():
    global game
    global total
    if game:
        game = False
    else:
        total = 150
        game = True
