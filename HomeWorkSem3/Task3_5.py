# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

print('Программа составляет список чисел Фибоначчи, в том числе для отрицательных индексов')

def input_data() -> int:
    while True:
        try:
            num = int(input('Введите число: '))
            if type(num) == int:
                return num
        except:
            print('Вы ввели не число.')


def my_fibonacci(num):
    fibonacci_lyst = [0, 1]

    for i in range(2, num):
        item = fibonacci_lyst[i - 2] + fibonacci_lyst[i - 1]
        fibonacci_lyst.append(item)
    return fibonacci_lyst


def my_negafibonacci(num):
    negafibonacci_lyst = [1, -1]
    num = abs(num)
    for i in range(2, num):
        item = negafibonacci_lyst[i-2] - negafibonacci_lyst[i-1]
        negafibonacci_lyst.append(item)
    return negafibonacci_lyst


number = input_data()
# if number > 0:
#     fib_lyst = my_fibonacci(number)
#     print(fib_lyst)
# else:
#     negafib_lyst = my_negafibonacci(number)
#     print(negafib_lyst)

fib_lyst = my_fibonacci(number)
negafib_lyst = my_negafibonacci(number)
negafib_lyst.reverse()
print(negafib_lyst + fib_lyst)