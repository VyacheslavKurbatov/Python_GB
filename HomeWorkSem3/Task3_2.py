# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint

print('Программа находит произведение пар чисел')


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
        # index = random.randint(0, 3)
        # num_list.append(round(random.uniform(0, 10), index))
        element = randint(0, 10)
        num_list.append(round(element, 2))
    return num_list


def product_numbers(some_list: list) -> list:
    product_num_list = []

    if len(some_list) % 2 == 1:
        len_some_list = int((len(some_list) / 2) + 1)
    else:
        len_some_list = int(len(some_list) / 2)

    for i in range(len_some_list):
        product_num = some_list[i] * some_list[len(some_list) - i - 1]
        product_num_list.append(product_num)
    return product_num_list


number = input_data()
number_list = fill_list(number)

print(f'{number_list} => {product_numbers(number_list)}')
