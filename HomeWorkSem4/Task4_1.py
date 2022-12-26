# 1. Задана натуральная степень k.
# 2. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и
# 3. записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

print('Программа формирует многочлен по заданому значению степени')


def input_data() -> int:
    while True:
        try:
            num = int(input('Введите натураьную степень: '))
            if type(num) == int:
                return num
        except:
            print('Натуральны это целые положительные числа.')


def formation_coefficient(degree: int) -> list:
    polinormal = []
    for i in range(degree + 1):
        coefficient = random.randint(-100, 100)
        if coefficient == 0:
            continue
        elif coefficient == 1:
            polinormal.append(f'x**{i}')
        else:
            polinormal.append(f'{coefficient}*x**{i}')
    if 'x**0' in polinormal[0]:
        polinormal[0] = polinormal[0].replace('*x**0', '')
    return polinormal


def formation_polynomial(some_list: list) -> str:
    some_list.reverse()
    some_string = ''
    for i in range(len(some_list)):
        if '-' in some_list[i]:
            some_string += ' - ' + some_list[i].replace('-', '')
        else:
            some_string += ' + ' + some_list[i]
    some_string = some_string[3:] + ' = 0'
    if '-' in some_list[0]:
        some_string = '-' + some_string
    return some_string


def writing_to_file(some_string: str):
    with open('Polinorm_file.txt', 'w') as data:
        data.writelines(f'{some_string}\n')


number = input_data()
coefficient_polinorm = formation_coefficient(number)
print(coefficient_polinorm)
polinorm = formation_polynomial(coefficient_polinorm)
print(polinorm)
writing_to_file(polinorm)
