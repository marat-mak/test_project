import timeit

def elapsed_time(func, size):
    return timeit.timeit(func % size, number=100)/100
code_append = """
elements = range(%d) # генератор элементов, которые будут вставляться в список
dict = {} # список, работу которого тестируем
for e in elements:
    dict[e] = e # добавляем каждый раз в конец
"""
for s in range(10,15):
    measure_1 = elapsed_time(code_append, 2**s)
    measure_2 = elapsed_time(code_append, 2**(s+1))
    print(measure_2,measure_1)
    ratio = measure_2 / measure_1
    print("[%d]/[%d] -> %5.2f" % (2**(s+1), 2**s, ratio))