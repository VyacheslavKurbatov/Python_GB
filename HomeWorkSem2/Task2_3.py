# Реализуйте алгоритм перемешивания списка.
from random import randint

print('Программа перемешивает список')


def input_data():
    while True:
        try:
            num = int(input('Введите число n равное длине списка: '))
            if num > 0:
                return num
            else:
                print('Длина списка не может быть текстом, дробным и отрицательным числом')
        except:
            print('Длина списка не может быть текстом, дробным и отрицательным числом')


def fill_list_random(num):
    num_list = []

    for i in range(num):
        element = randint(-100, 100)
        num_list.append(round(element, 2))
    return num_list


def shuffling_list(some_list):
    other_list = []
    len_some_list = len(some_list)

    while len_some_list > 0:
        rnd_index = randint(0, len_some_list)
        digit = some_list.pop(rnd_index - 1)
        other_list.append(digit)
        len_some_list -= 1
    return other_list


number = input_data()
number_list = fill_list_random(number)
print(number_list)

shuffl_list = shuffling_list(number_list)
print(shuffl_list)
