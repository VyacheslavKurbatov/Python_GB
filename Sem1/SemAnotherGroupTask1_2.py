# a = 23
# b = 45
# a,b = b,a # вариант замены a и b
# print(a)
# print(b)

# 1. Напишите программу, котороая принимает на вход два числа и проверяетБ является ли одно число квадратом другого
# 2. Напишите программу, которя на вход принимает 5 чисел и находит максимальное из них.

# Задание 1
# num1 = int(input('введите число 1 = '))
# num2 = int(input('введите число 2 = '))
#
# print(f'{num1}, {num2} -> ', end=' ') # end=' ' для того чтобы на одной строке было с yes/no
#
# if num2 == num1 ** 2 or num1 == num2 ** 2:
#     print('yes')
# else:
#     print('no')

# Задание 2 вариан 1
# num1 = int(input('number 1 = '))
# num2 = int(input('number 2 = '))
# num3 = int(input('number 3 = '))
# num4 = int(input('number 4 = '))
# num5 = int(input('number 5 = '))
#
# max_num = num1
#
# Задание 2 вариан 2
# if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:
#     print(f'{num1} max')
# if num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
#     print(f'{num2} max')
# if num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:
#     print(f'{num3} max')
# if num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:
#     print(f'{num4} max')
# if num5 > num1 and num5 > num2 and num5 > num3 and num5 > num4:
#     print(f'{num5} max')
#
# Задание 2 вариан 3
# if num2 > max_num:
#     max_num = num2
# if num3 > max_num:
#     max_num = num3
# if num4 > max_num:
#     max_num = num4
# if num5 > max_num:
#     max_num = num5
#
# print(max_num)


# Задание 2 вариан 4

# numbers = []
#
# for _ in range(5):
#     numbers.append(int(input(f'Введите элемент под номером {i + 1} : ')))
# print(numbers)
# print(max(numbers))

# Задание 2 вариан 5 (вводим число, сравниваем его с макс, если меньше не запоминаем его и вводим следующее)
my_max = 0
for _ in range(5): #нижнее подчеркивание вместо переменной i. "_" используют если переменная больше нигде не используется
    num = int(input('Введите число '))
    if my_max < num:
        my_max = num
print(my_max)

# range(5) -> range(start=0, stop=5, step=1)
# range(1,5) -> range(start=1, stop=5, step=1)
# range(1,9,2) -> range(start=1, stop=9, step=2)
# range(9,1,-1) -> range(start=9, stop=1, step=-1) # отсчет в обратную сторону