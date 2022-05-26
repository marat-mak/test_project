def den_func(a,n):
    if a % n == 0:
        print(f"Число {n} является делителем числа {a}")
    else:
        print(f"Число {n} не является делителем числа {a}")
while True:
    a = int(input('Введите делимое:\n'))
    n = int(input('Введите делитель:\n'))
    if a == 0 or n == 0:
        break
    den_func(a,n)

