# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

statementsX = [False, True]
statementsY = [False, True]
statementsZ = [False, True]

# statement1 = statementsX[0] | statementsX[0]
# print(statementsX[0])
# print(statementsX[0])
# print(statement1)
for x in statementsX:
    for y in statementsY:
        for z in statementsZ:
            statement1 = not (x | y | z)
            statement2 = (not x) & (not y) & (not z)
            print(f' 1 {statement1}', end=' ')
            print(f' 2 {statement2}', end=' ')
            if statement1 == statement2:
                print('Утверждение истинно')
            else:
                print("Утверждение не истинно")

