import time

N = 100
def decorator_time(fn):
   def wrapper():
       print(f"Запустилась функция {fn}")
       t0 = time.time()
       result = fn()
       dt = time.time() - t0
       print(f"Функция выполнилась. Время: {dt:.10f}")
       return dt  # задекорированная функция будет возвращать время работы
   return wrapper

@decorator_time
def pow_2():
    return 999999 ** 999999
@decorator_time
def in_build_pow():
    return pow(999999, 999999)

pow_2()
in_build_pow()