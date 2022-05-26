def den_count(a):
    count = 0
    for i in range(1,a+1):
        if a % i == 0:
            count += 1
    return count
max_count = 0
for e in range(10000):
    if den_count(e) > max_count:
        max_count = den_count(e)
        max_num = e
print(max_num)
print(max_count)

