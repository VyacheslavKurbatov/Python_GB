# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

print('Программа преобразует десятичное число в двоичное')


def input_data() -> int:
    while True:
        try:
            num = int(input('Введите число: '))
            if type(num) == int:
                return num
        except:
            print('Вы ввели не число.')


def conversion_to_binary(num: int):
    x = 0
    res = 0

    while num > 0:
        x = (x * 10) + (num % 2)
        num = int((num / 2))
        if x == 0:
            x = 2

    while x > 0:
        remnant = x % 10
        res = res * 10 + remnant
        x = int(x / 10)

    if res % 10 == 2:
        res = int(res / 10);
        res *= 10;
    return res


number = input_data()
binary_number = conversion_to_binary(number)
print(f'число {number} в двоичной системе = {binary_number}')
