from datetime import datetime
import time  # проверять действие измерителя будем с помощью библиотеки time
from datetime import datetime
import time

from contextlib import contextmanager
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
    return time.sleep(2)
@decorator_time
def in_build_pow():
    return time.sleep(2)

# pow_2()
# in_build_pow()




class Timer:
    def __init__(self):
        pass

    def __enter__(
            self):  # этот метод вызывается при запуске с помощью with. Если вы хотите вернуть какой-то объект, чтобы потом работать с ним в контекстном менеджере, как в примере с файлом, то просто верните этот объект через return
        self.start = datetime.utcnow()
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):  # этот метод срабатывает при выходе из контекстного менеджера
        print(f"Time passed: {(datetime.utcnow() - self.start).total_seconds()}")

@contextmanager  # оборачиваем функцию в декоратор contextmanager
def timer():
    start = datetime.utcnow()
    yield  # если вам нужно что-то вернуть через контекстный менеджер, просто вставьте этот объект сюда.
    print(f"Time passed: {(datetime.utcnow() - start).total_seconds()}")

with Timer():
    time.sleepw(2)