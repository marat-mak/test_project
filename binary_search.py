def binary_search(list, item):
    low = 0
    high = len(list) - 1
    count = 0
    while low <= high:
        count += 1
        # print(f'{count} попыток')
        mid = (low + high) // 2
        guess = list[mid]
        print(f'Предположение: {guess}')
        if guess == item:
            print(f'{count} попыток')
            return mid
        elif item < guess:
            high = mid - 1
        else:
            low = mid + 1
    print(f'{count} попыток')
    return None

my_list = [i for i in range(1,100)]
# print(my_list)
print(binary_search(my_list, 99))

