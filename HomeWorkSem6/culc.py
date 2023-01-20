data_1 = '2+2'
data_2 = '1+2*3'
data_3 = '1-2*3'
data_4 = '-2*3 - 4* -5'


def input_data(text):
    data = input(text)

    data = data.replace(' ', '').replace('+', ' + ').replace('-', ' - ').replace('/', ' / ').replace('*', ' * ')
    print(data)
    for i, item in enumerate(data):
        if data[0] == ' ' and data[1] == '-':
            data = data[3:]
            data = '-' + data
    data = data.split()
    return data


operation = \
    {
        '+': lambda a, b: float(a) + float(b),
        '-': lambda a, b: float(a) - float(b),
        '*': lambda a, b: float(a) * float(b),
        '/': lambda a, b: float(a) / float(b),
    }


def arithmetic_operation(oper, a, b):
    result = operation[oper](a, b)
    return result


def change_data(data: list, index: int, num: int):
    data[index - 1] = num
    data.pop(index)
    data.pop(index)
    return data


def mult_div(data: list):
    for i, item in enumerate(data):
        if item in '*/':
            res = arithmetic_operation(data[i], data[i - 1], data[i + 1])
            data = change_data(data, i, res)
    data = list(map(lambda x: str(x), data))
    return data


def addit_sub(data: list):
    for i, item in enumerate(data):
        if item in '+-':
            res = arithmetic_operation(data[i], data[i - 1], data[i + 1])
            data = change_data(data, i, res)
    data = list(map(lambda x: str(x), data))
    return data


data_list = input_data('Введите пример: ')

for item in operation.keys():
    while item in data_list:
        data_list = mult_div(data_list)
        data_list = addit_sub(data_list)

print(data_list)


