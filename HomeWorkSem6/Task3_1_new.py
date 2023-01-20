from random import randint

print('Программа находит сумму элементов, стоящих на нечетных позициях')


def input_data():
    while True:
        try:
            num = int(input('Введите длинну списка: '))
            if type(num) == int:
                return num
        except:
            print('Вы ввели не число.')


# def fill_list(num):
#     num_list = []
#
#     for i in range(num):
#         element = randint(-100, 100)
#         num_list.append(round(element, 2))
#     return num_list
#
#
# def sum_number(some_list):
#     sum_num = 0
#     for i in range(1, len(some_list), 2):
#         sum_num += some_list[i]
#     return sum_num
#
#
# def uneven_num_list(num_list):
#     uneven_num = []
#     for i in range(1, len(num_list), 2):
#         if i % 2 == 1:
#             uneven_num.append(num_list[i])
#     return uneven_num

# number = input_data()
# number_list = fill_list(number)
# uneven_number = uneven_num_list(number_list)
# sum_uneven_number = sum_number(number_list)
#
# print(f'{number_list} -> на нечётных позициях элементы {uneven_number}, ответ: {sum_uneven_number}')


def new_prog(num):
    some_list = [randint(-100, 100) for i in range(num)]

    res = 0
    for i, item in enumerate(some_list):
        if i % 2 == 1:
            res += item
    return res, some_list


number = input_data()

result, rnd_list = new_prog(number)

print(f'{rnd_list} -> сумма нечетных элементов: {result}')