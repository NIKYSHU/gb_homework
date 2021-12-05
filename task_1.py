def odd_nums(num):
    for i in range(1, num + 1, 2):
        yield i
odd_to_15 = odd_nums(15)
print(odd_to_15)
print(next(odd_to_15))
print(next(odd_to_15))
next(odd_to_15)
next(odd_to_15)
next(odd_to_15)
next(odd_to_15)
next(odd_to_15)
print(next(odd_to_15))