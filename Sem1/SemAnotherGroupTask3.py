# Напишите программу, котороя будет на вход принимать число N и выводить числа от -N до N

n = int(input('Input number = '))
if n < 0:
    n *= -1
for i in range(-n, n + 1):
    print(f'{i};', end=' ')
