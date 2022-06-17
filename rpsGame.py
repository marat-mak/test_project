import random, sys

print('Камень ножницы бумага'.upper())
wins = 0
losses = 0
draws = 0
games = 0
while True:
    print(f'Побед: {wins}, поражений: {losses}, ничьих: {draws} | Игр сыграно: {games}')
    games += 1
    while True:

        print('Ваш ход: (к)амень (н)ожницы (б)умага | (в)ыход')
        player_move = input()

        if player_move == 'в':
            sys.exit()
        if player_move == 'к' or player_move == 'н' or player_move == 'б':
            break

    if player_move == 'к':
        print('Камень и ')
    if player_move == 'н':
        print('Ножницы и ')
    if player_move == 'б':
        print('Бумага и ')

    computer_move = random.randint(1,3)
    if computer_move == 1:
        computer_move = 'к'
        print('камень')
    if computer_move == 2:
        computer_move = 'н'
        print('ножницы')
    if computer_move == 3:
        computer_move = 'б'
        print('бумага')

    if player_move == computer_move:
        draws += 1
        print('Ничья')
    if player_move == 'к' and computer_move == 'н':
        wins += 1
        print('Вы выиграли!')
    if player_move == 'н' and computer_move == 'б':
        wins += 1
        print('Вы выиграли!')
    if player_move == 'б' and computer_move == 'к':
        wins += 1
        print('Вы выиграли!')
    if player_move == 'к' and computer_move == 'б':
        losses += 1
        print('Вы проиграли!')
    if player_move == 'н' and computer_move == 'к':
        losses += 1
        print('Вы проиграли!')
    if player_move == 'б' and computer_move == 'н':
        losses += 1
        print('Вы проиграли!')