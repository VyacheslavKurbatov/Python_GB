# 1. Напишите программу, которая принимает на вход два числа и
# проверяет, является ли одно число квадратом другого.
# *Примеры: *
#
# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8, 9 -> нет
# import random

# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
#
# if num2 == num1 ** 2 or num1 == num2 ** 2:
#     print(f'{num1} , {num2} -> да')
# else:
#     print(f'{num1} , {num2} -> нет')

# 2.Напишите программу, которая на вход принимает 5 чисел и находит
# максимальное из них.
# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

# count_num = int(input("Enter index --> "))
# list_num = []
#
# for i in range(count_num):
#     num = int(input(f"Enter num {i + 1} --> "))
#     list_num.append(num)
#
# max_num_list = max(list_num)
# print(max_num_list)

# my_List = []
#
# for i in range(5): # range(a, b, c) a-начало, b-конец(не включительно), с-шаг
#     my_List.append(int(input('введите число'))) # .append - наполняет список

# my_max = my_List[0]
#
# for item in my_List: # item - элементы а не индексы
#     if my_max < item:
#         my_max = item
# print(f'максимальное занчение списка = {my_max}')

my_List = []

for i in range(5):
    my_List.append(random.randint(0,100))

print(my_List)