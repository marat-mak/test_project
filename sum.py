def adder(*nums):
    sum_ = 0
    for n in nums:
        sum_ += n

    return sum_
nums=map(int,tuple(input()))

print(adder(*nums))