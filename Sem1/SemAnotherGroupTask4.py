# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# вариант 1

# num = input('Input number: ')
# if '.' in num:
#     index = num.find(',')+1
#     print(num[index])
# elif ',' in num:
#     index = num.find(',') + 1
#     print(num[index])
# else:
#     print('no')

# вариант 2

# num = float(input('Input number = '))
# if num % 1 == 0:
#     print('no')
# else:
#     num = int(num * 10 % 10)
#     print(num)

# вариант 3

# num = float(input('Input number = '))
# if type(num) == int:
#     print('no')
# else:
#     num = int(num * 10 % 10)
#     print(num)

num = input('Input number = ')
if num.isdigit():
    print('no')
else:
    num = int(float(num) * 10 % 10)
    print(num)