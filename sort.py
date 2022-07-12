import random

a = [i for i in range(5000)]
array = list(reversed(a))
# for i in range(len(array)): # проходим по всему массиву
#         idx_max = i # сохраняем индекс предположительно минимального элемента
#         for j in range(i+1, len(array)):
#                 if array[j] > array[idx_max]:
#                         idx_max = j
#         if i != idx_max: # если индекс не совпадает с минимальным, меняем
#                 array[i], array[idx_max] = array[idx_max], array[i]
# print(array)
#
#
# for i in range(len(array)):
#         for j in range(len(array) - i - 1):
#                 if array[j] > array[j + 1]:
#                         array[j], array[j + 1] = array[j + 1], array[j]
# print(array)
#
#
# count = 0
#
# for i in range(1, len(array)):
#     x = array[i]
#     idx = i
#
#     while idx > 0:
#         count += 1
#         if not (array[idx-1] > x):
#             break
#
#         array[idx] = array[idx-1]
#         idx -= 1
#     array[idx] = x
# print(array)
#
#
# def merge_sort(L):  # «разделяй»
#     if len(L) < 2:  # если кусок массива равен 2,
#         return L[:]  # выходим из рекурсии
#     else:
#         middle = len(L) // 2  # ищем середину
#         left = merge_sort(L[:middle])  # рекурсивно делим левую часть
#         right = merge_sort(L[middle:])  # и правую
#         return merge(left, right)  # выполняем слияние
#
#
# def merge(left, right):  # «властвуй»
#     result = []  # результирующий массив
#     i, j = 0, 0  # указатели на элементы
#
#     # пока указатели не вышли за границы
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#
#     # добавляем хвосты
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#
#     return result


def qsort(array, left, right):
    middle = (left + right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)


def qsort_random(array, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1
    p = random.choice(array[left:right + 1])
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort_random(array, left, j)
    if right > i:
        qsort_random(array, i, right)

qsort(array,0,len(array)-1)
print(array)
