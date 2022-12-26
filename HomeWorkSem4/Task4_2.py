# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

print('Программа считает сумму многочленов')


def reading_to_file(text: str) -> str:
    with open(f'{text}', 'r') as data:
        for polinorm in data:
            return polinorm


def create_coefficient(polinorm: str) -> dict:
    new_polinorm = polinorm.replace(' ', '').replace('=0', '').replace('+', ' ').replace('-', ' -')
    new_polinorm = new_polinorm.split()
    polinorm_dict = {}

    for item in new_polinorm:
        if 'x' not in item:
            polinorm_dict[0] = int(item)
        elif item.startswith('x'):
            item_list = item.split('**')
            polinorm_dict[int(item_list[1])] = 1
        elif item.startswith('-x'):
            item_list = item.split('**')
            polinorm_dict[int(item_list[1])] = -1
        else:
            item_list = item.split('**')
            coefficient = item_list[0].split('*')
            polinorm_dict[int(item_list[1])] = int(coefficient[0])

    return polinorm_dict


def sum_coefficient(some_dict_1: dict, some_dict_2: dict) -> dict:
    sum_dict = {}
    kyes_dict = set(list(some_dict_1.keys()) + list(some_dict_2.keys()))

    for kye in kyes_dict:
        vers_1 = some_dict_1.get(kye)
        vers_2 = some_dict_2.get(kye)
        if vers_1 == None:
            vers = vers_2
        elif vers_2 == None:
            vers = vers_1
        else:
            vers = vers_1 + vers_2
        sum_dict[kye] = vers
    return sum_dict


def sum_polinorm(some_dict: dict) -> list:
    some_list = []
    for item in some_dict:
        if item == 0:
            some_list.append(f'{some_dict.get(item)}')
        elif item == 1:
            some_list.append(f'{some_dict.get(item)}*x')
        else:
            some_list.append(f'{some_dict.get(item)}*x**{item}')

    return some_list


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
    with open('sup_polinorm_file.txt', 'w') as data:
        data.writelines(f'{some_string}\n')


polinorm_1 = reading_to_file('Polinorm_file.txt')
print(polinorm_1)

polinorm_2 = reading_to_file('Polinorm2_file.txt')
print(polinorm_2)

polinorm_1_list = create_coefficient(polinorm_1)
print(polinorm_1_list)

polinorm_2_list = create_coefficient(polinorm_2)
print(polinorm_2_list)

sum_coefficient_polinorm = sum_coefficient(polinorm_1_list, polinorm_2_list)
print(sum_coefficient_polinorm)

sum_polinorm = sum_polinorm(sum_coefficient_polinorm)
print(sum_polinorm)

polynomial_result = formation_polynomial(sum_polinorm)
print(polynomial_result)

writing_to_file(polynomial_result)

