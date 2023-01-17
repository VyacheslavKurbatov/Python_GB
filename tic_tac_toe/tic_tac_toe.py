import os

new_playing_field = [1, 2, 3, 4, 5, 6, 7, 8, 9, '-']
playing_field = new_playing_field

win_pos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

clear = lambda: os.system('cls')

game_stat = False
player_one = True
player_two = False




def print_playing_field():
    clear()
    print(playing_field[0], end=' | ')
    print(playing_field[1], end=' | ')
    print(playing_field[2])
    print(playing_field[9], end=' ')
    print(playing_field[9], end=' ')
    print(playing_field[9], end=' ')
    print(playing_field[9], end=' ')
    print(playing_field[9])
    print(playing_field[3], end=' | ')
    print(playing_field[4], end=' | ')
    print(playing_field[5])
    print(playing_field[9], end=' ')
    print(playing_field[9], end=' ')
    print(playing_field[9], end=' ')
    print(playing_field[9], end=' ')
    print(playing_field[9])
    print(playing_field[6], end=' | ')
    print(playing_field[7], end=' | ')
    print(playing_field[8])


def input_data(text1: str, text2: str, elem1, elem2):
    while True:
        try:
            elem = input(text1)
            if elem == elem1 or elem == elem2:
                return elem
            print(text2)
            print('')
        except:
            print(text2)

def input_step(text1: str, text2: str):
    global playing_field
    while True:
        try:
            elem = int(input(text1))
            if elem in playing_field:
                return elem
            print(text2)
            print('')
        except:
            print(text2)


def choos_side():
    one = input_data('Чем будет играть 1ый игрок? (введите "х" или "о") : ',
                     'Введите "х" или "о" в английской раскладке, другого не примет',
                     'x',
                     'o')
    if one == 'x':
        two = 'o'
    else:
        two = 'x'
    return one, two


def new_game():
    global game_stat
    global playing_field
    if game_stat:
        game_stat = False
    else:
        playing_field = new_playing_field
        game_stat = True

def change_step():
    global player_one
    if player_one:
        player_one = False
    else:
        player_one = True


def check_win():
    win_side = ''
    global win_pos
    global playing_field

    for i in win_pos:
        if playing_field[i[0]] == 'x' and playing_field[i[1]] == 'x' and playing_field[i[2]] == 'x':
            win_side = 'x'
        if playing_field[i[0]] == 'o' and playing_field[i[1]] == 'o' and playing_field[i[2]] == 'o':
            win_side = 'o'
    return win_side


def game():
    count = 0
    print('Это игра в крестики - нолики')
    ng = input_data('Начать новую игру? Y/N: ',
                    'Для ответа "да" введи заглавную Y, для "нет" введи N',
                    'Y',
                    'N')
    if ng == 'Y':
        clear()
        print('Канайтесь')
        print('')
        player_one_ind, player_two_ind = choos_side()
        new_game()
    else:
        print('Ну как хочешь.')

    while game_stat == True:
        print_playing_field()
        if count == 9:
            print('Победила дружба !!! :P')
            break
        if player_one:
            print('Ходит ПЕРВЫЙ игрок')
            step = input_step('Введите номер ячеки хода: ', 'Такой ячейки нет, или она уже занята, попробуй еще раз.')
            playing_field[step - 1] = player_one_ind
            if check_win() == player_one_ind:
                print_playing_field()
                print('Победил ПЕРВЫЙ игрок!!!')
                new_game()
            else:
                count += 1
                print(count)
                change_step()
        else:
            print('Ходит ВТОРОЙ игрок')
            step = input_step('Введите номер ячеки хода: ', 'Такой ячейки нет, или она уже занята, попробуй еще раз.')
            playing_field[step - 1] = player_two_ind
            if check_win() == player_two_ind:
                print_playing_field()
                print('Победил ВТОРОЙ игрок!!!')
                new_game()
            else:
                count += 1
                print(count)
                change_step()


game()