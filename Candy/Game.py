max_total = 150
total = max_total
game = False
bot_level = 'Light'

def get_total():
    global total
    return total

def set_total_to_max():
    global total
    global max_total
    total = max_total


def take_candies(take: int):
    global total
    total -= take


def set_max_total(value: int):
    global max_total
    max_total = value


def check_game():
    global game
    return game


def new_game():
    global game
    global total
    if game:
        game = False
    else:
        total = max_total
        game = True


def change_level():
    global bot_level
    if bot_level == 'Light':
        bot_level = 'Hard'
    else:
        bot_level = 'Light'


def get_bot_level():
    global bot_level
    return bot_level