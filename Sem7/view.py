def main_menu() -> int:
    print('Главное меню.')
    menu_list = ['Показать все контакты',
                 'Открыть файл',
                 'Сохранить файл',
                 'Создать контакт',
                 'Изменить контакт',
                 'Удалить контакт',
                 'Выход'
                 ]
    for i in range(len(menu_list)):
        print(f'\t{i + 1}. {menu_list[i]}')
    while True:
        try:
            user_input = int(input('Введи № команды >: '))
            if  1 <= user_input <= 7:
                return user_input
            else:
                print('Такой команды нет')
        except:
            print('Такой команды нет')

def show_all(db: list):
    if db_success(db):
        for i in range(len(db)):
            user_id = i + 1
            print(f'\t{user_id}', end='. ')
            for v in db[i].values():
                print(f'{v}', end=' ')
            print()


def db_success(db: list):
    if db:
        print('Телефонная книга открыта')
        return True
    else:
        print('Телефонная книга пуста или не открыта')
        return False


def exit_program():
    print('Завершение программы.')
    exit()


create_contact_contact_text = ['Создание нового контакта.',
                               'Введите фамилию >: ',
                               'Введите имя >: ',
                               'Введите телефон >: ',
                               'Введите комментарий >: ']


def print_safe():
    print('Файл сохранен')


chage_contact_text = ['Какой контакт вы хотите изменить?: ',
                      'Введите номер контакта, который нужно изменить.',
                      'Введите фамилию >: ',
                      'Введите имя >: ',
                      'Введите телефон >: ',
                      'Введите комментарий >: ']

delete_contact_text = ['Какой контакт вы хотите изменить?: ',
                      'Такого контакта нет',
                      'Контакт удален.']