# 3. Создайте словать заданный по формуле 3 * n + 1, где n это ключ, а формула значение
#
# *Пример: *
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
my_dict = {}

number = int(input('введите целое число: '))
for n in range(1, number + 1):
    my_dict[n] = 3*n + 1

print(my_dict)
print(my_dict.get(4, 'Такого ключа нет'))

my_string = 'Питон самый лучший язык в мире'

my_string1 = my_string.split('и')
print(my_string1)

my_string1 = my_string.replace('и', '')
print(my_string1)

print(my_string.startswith('пит'))
print(my_string.lower().startswith('пит'))
print(my_string.upper().startswith('ПИТ'))
print(my_string.upper().endswith('ире'))

my_list = ['1','2','34','5','6','7','8']
print(' '.join(my_list))
