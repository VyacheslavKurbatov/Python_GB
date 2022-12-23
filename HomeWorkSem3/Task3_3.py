# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random

print('Программа находит разницу между максимальным и минимальным значением дробной части')


def input_data() -> int:
    while True:
        try:
            num = int(input('Введите длинну списка: '))
            if type(num) == int:
                return num
        except:
            print('Вы ввели не число.')


def fill_list(num: int) -> list:
    num_list = []

    for i in range(num):
        index = random.randint(0, 3)
        num_list.append(round(random.uniform(0, 10), index))
    return num_list


def find_max_min(some_list: list):
    float_part = []

    for i in range(len(some_list)):
        _ = str(some_list[i])
        item = _.split('.')
        if len(item[1]) == 1:
            item[1] += '00'
            float_part.append(int(item[1]))
        elif len(item[1]) == 2:
            item[1] += '0'
            float_part.append(int(item[1]))
        else:
            float_part.append(int(item[1]))

    max_item = float_part[1]
    min_item = float_part[1]
    for i in range(len(float_part)):
        if float_part[i] == 0:
            continue
        elif float_part[i] > max_item:
            max_item = float_part[i]
        elif float_part[i] < min_item:
            min_item = float_part[i]
    return max_item, min_item


def difference(max, min):
    diff = max - min
    diff = float('0.' + str(diff))
    return diff

number = input_data()
number_list = fill_list(number)
print(number_list)
max, min = find_max_min(number_list)
result = difference(max, min)
print(f'{number_list} => max = 0.{max}, min = 0.{min}, разница = {result}')

