# Найдите корни квадратного уравнения Ax² + Bx + C = 0
# с помощью математических формул нахождения корней квадратного уравнения


equation = 'x**2 + 4 * x + 4'.replace(" ", '')
print(equation)
mid_split = equation.replace("*", '').split("x")
mid_split[1] = mid_split[1].replace("2", '')

print(mid_split)

for i in range(len(mid_split)):
    if mid_split[i] != '':
        mid_split[i] = int(mid_split[i])
    else:
        mid_split[i] = 1
print(mid_split)

a = mid_split[0]
b = mid_split[1]
c = mid_split[2]

d = b ** 2 - 4 * a * c

if d > 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print(f"x1 = {x1},x2 = {x2}")
elif d == 0:
    x = (-b) / (2 * a)
    print(f"x = {x}")
else:
    print("Корней нет")
