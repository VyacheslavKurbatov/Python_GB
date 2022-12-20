# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

text = ['Text', 'sdgkgsdg', ';sdkgs;', ';sdkg45']
search = 'sd'

for i in range(0, len(text)):
    if search in text[i]:
        print(f'В элементе с индексом {i} - Да')


# for i in range(0, len(text)):
#     if text[i].find(search) != -1:
#         print(f'В элементе с индексом {i} - Да')