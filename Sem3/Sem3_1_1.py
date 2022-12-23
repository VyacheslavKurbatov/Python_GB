import math

equation = 'x**2 + 3 * x - 4 = 0'


def create_koef(equation: str):
    new_equation = equation.replace(' ', '').replace('=0', '').replace('+', ' ').replace('-', ' -')
    new_equation = new_equation.split()
    new_list = []
    for item in new_equation:
        if item.startswith('x'):
            new_list.append(1)
        elif item.startswith('-x'):
            new_list.append(1)
        else:
            new_list.append(item.split('*x')[0])
    return new_list


def solve_equation(koef):
    a, b, c = int(koef[0]), int(koef[1]), int(koef[2])
    d = b ** 2 - 4 * a * c

    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return round(x1, 2), round(x2, 2)
    elif d == 0:
        x = (-b) / (2 * a)
        return round(x, 2)
    else:
        return 'корней нет'


print(solve_equation(create_koef(equation)))
