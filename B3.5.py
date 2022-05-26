print('Что надеть?')
temp = int(input('Введите температуру:\n'))
if 20<temp<30:
    isRain = input('Есть осадки?\n').lower()=='да'
    if isRain:
        print('Футболку, шорты и дождевик')
    else:
        print('Футболку и шорты')
else:
    if 0<temp<=20:
        isRain = input('Есть осадки?\n').lower()=='да'
        if isRain:
            isRain = input('Осадки сильные?\n').lower()=='да'
            if isRain:
                print('Пальто, резиновые сапоги и зонт')
            else:
                print('Пальто и дождевик')
        else:
            print('Пальто')
    elif temp<=0:
        print('Пуховик')
    else:
        print('Сиди дома!')
