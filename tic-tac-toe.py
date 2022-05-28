field = [[' '] * 3 for i in range(3)]
def show():
    print()
    print('     0   1   2   ')
    print('   -------------')
    for i, row in enumerate(field):
        print(f'{i}  | {" | ".join(row)} |')
        print('   -------------')
    print()

def ask(user):
    while True:
        cords = input(f'Ходит {user}, введите строку и столбец через пробел: ').split()
        if len(cords) != 2:
            print('Введите 2 координаты!')
            continue
        x, y = cords
        if not (x.isdigit()) or not (y.isdigit()):
            print('Введите числа!')
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print('Координаты вне диапазона!')
            continue
        if field[x][y] != ' ':
            print('Клетка занята!')
            continue
        return x, y

def check_win():
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[i][j])
        if symbols == [user, user, user]:
            return True

    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[j][i])
        if symbols == [user, user, user]:
            return True
    symbols = []
    for i in range(3):
        symbols.append(field[i][i])
        if symbols == [user, user, user]:
            return True
    symbols = []
    for i in range(3):
        symbols.append(field[i][2-i])
        if symbols == [user, user, user]:
            return True
    return False

num = 0
while True:
    num += 1
    show()
    if num % 2 == 0:
        user = '0'
    else:
        user = 'X'
    x, y = ask(user)
    if num % 2 == 0:
        field[x][y] = user
    else:
        field[x][y] = user
    if check_win():
        show()
        print(f'Выиграл {user}!')
        break
    if num == 9:
        print('Ничья!')
        break