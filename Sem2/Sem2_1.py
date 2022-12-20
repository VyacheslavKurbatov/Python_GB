# 3. Напишите программу, которая определит позицию второго
# вхождения строки в списке либо сообщит, что её нет.
#
# *Пример:*
#
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1
import random

# text = ["йцу", "фыв", "ячс", "цук", "йцукен"]
# search = "йцу"
#
# position = 2
# count = 0
#
#
# def find_text(list, position):
#     count = 0
#     for i in range(0, len(text)):
#         if search in text[i]:
#             if count == position:
#                 return i
#                 break
#             else:
#                 count += 1
#     if count < position:
#         return -1
#
#
# response = find_text(text, position)
# print(response)

# my_list.index(my_str, my_list.index(my_str))

my_list = []

for _ in range(10):
    index = random.randint(0, 3)
    my_list.append(random.uniform(0, 10), index)

print(my_list)
