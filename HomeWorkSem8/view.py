def input_class() -> str:
    print('Элктронный журнал.')
    print('(для выхода из программы введите exit)')
    user_input = input('Введи класс >: ').lower()

    return user_input

def second_menu() -> int:
    print('_______________')
    menu_list = ['Занятие',
                 'Успеваемость ученика',
                 'Выход'
                 ]
    for i in range(len(menu_list)):
        print(f'\t{i + 1}. {menu_list[i]}')
    user_input = int(input('Введи команду >: '))

    return user_input

def lesson_menu() -> str:
    print('Элктронный журнал.')

    user_input = input('Введи урок >: ').lower()

    return user_input


def all_student(student_dict):
    for key, value in student_dict.items():

        average_value = sum(value) / len(value)
        print(f'{key} \tоценки: {value} \tоценка за четверть: {round(average_value, 2)}')


def who_answer():
    return input('Кто будет отвечать (для выхода введите exit)? : ')


def what_mark():
    try:
        num = int(input('На какую оценку? : '))
        if  1 <= num <= 5:
            return num
    except:
        print('Введите число о 1 до 5')

def statistics(student_dict):
    student = input('Имя ученика (для выхода введите exit): ')

    if student == 'exit':
        return student
    for key, value in student_dict.items():
        average_value = 0
        for k, v in value.items():
            if k == student:
                average_value = sum(v) / len(v)
        print(f'{key}: \t{value.get(student)} \tоценка за четверть: {round(average_value, 2)}')


mistake = [' ', '_____________', 'Такого класса нет']