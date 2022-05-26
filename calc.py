def get_mul_func(m):
    nonlocal_m = m

    def local_mul(n):

        return n * nonlocal_m

    return local_mul


two_mul = get_mul_func(2.54)  # возвращаем функцию, которая будет умножать числа на 2
print(two_mul(1))