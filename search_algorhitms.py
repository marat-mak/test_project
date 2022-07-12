def find(array, element):
    for i, a in enumerate(array):
        if a == element:
            return i
    return False

def count(array, element):
    count = 0
    for i in array:
        if i == element:
            count += 1
    return count

def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (left + right) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

element = int(input('Введите искомое число:\n'))
array = [i for i in range(1,100)]
print(binary_search(array, element, 0, 98))