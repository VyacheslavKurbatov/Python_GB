# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
import math

# print('Программа считает сумму цифр в введенном числе')
#
#
# def input_data():
#     while True:
#         try:
#             num = float(input('Введите число: '))
#             if type(num) == float:
#                 return num
#         except:
#             print('Вы ввели не число.')
#
#
# def sum_digits(num):
#     num = abs(num)
#     num_str = str(num)
#     num_str = num_str.replace('.', '')
#     result = 0
#     for i in range(0, len(num_str), 1):
#         num = int(num_str[i])
#         result += num
#     return result
#
#
# number = input_data()
# res = sum_digits(number)
# print(f'Сумма цифр в числе {number} = {res}')


def input_data():
    while True:
        try:
            num = float(input('Введите число: '))
            if type(num) == float:
                return num
        except:
            print('Вы ввели не число.')


def sum_digits(num):
    num = str(num)
    num = num.replace('-', '').replace('.', '').replace('', ' ')
    num = list(map(lambda x: int(x), num.split()))
    res = 0
    for i, item in enumerate(num):
        res += item
    return res


number = input_data()
result = sum_digits(number)
print(f'Сумма цифр в числе {number} = {result}')