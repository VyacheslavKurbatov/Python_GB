# Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

print('Программа считает сумму чисел в списке')


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


def fill_list(num):
    num_list = []

    for i in range(num):
        element = (1 + 1 / (i + 1)) ** (i + 1)
        num_list.append(round(element, 2))
    print(f'Для n = {num} -> {num_list}')
    return num_list


def sum_numbers_in_list(numbers_list):
    sum_num = 0
    for i in numbers_list:
        sum_num += i
    print(f'Сумма = {sum_num}')


number = input_data()
number_list = fill_list(number)
sum_numbers_in_list(number_list)
