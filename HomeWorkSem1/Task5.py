# Напишите программу,
# 1. которая принимает на вход координаты двух точек и
# 2. находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math

numAX = int(input('Введите координату X точки A = '))
numAY = int(input('Введите координату Y точки A = '))

numBX = int(input('Введите координату X точки B = '))
numBY = int(input('Введите координату Y точки B = '))

distance = math.sqrt((numAX - numBX)**2 + (numAY - numBY)**2)
print(f'Расстояние между А ({numAX},{numAY}) и В ({numBX}, {numBY}) -> {round(distance, 3)}')
