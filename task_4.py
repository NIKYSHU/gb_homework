from time import perf_counter

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

start = perf_counter()
result = [el for el in set(src) if src.count(el) == 1]
print(result)
print('время выполнения 1: ', perf_counter() - start)


start = perf_counter()
result = set()
tmp = set()
for el in src:
    if el not in tmp:
        result.add(el)
    else:
        result.discard(el)
    tmp.add(el)
print([*result])
print('время выполнения 2: ', perf_counter() - start)