#Игра в угадывание чисел
import random
secret_number = random.randint(1,20)

guess_count = 0
for g in range(4):
    guess_number = int(input(f'Я загадал число от 1 до 20. Попыток осталось: {4-guess_count}\n'))
    guess_count += 1
    if guess_number < secret_number:
        print('Загаданное число больше')
    elif guess_number > secret_number:
        print('Загаданное число меньше')
    else:
        break
if guess_number == secret_number:
    print(f'Вы угадали число! Количество попыток: {guess_count}')
else:
    print('Вы не угадали. Я загадал число: '+ str(secret_number))
