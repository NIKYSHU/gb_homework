from time import perf_counter
import sys

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

start = perf_counter()
result = [ex for el, ex in zip(src, src[1:]) if el < ex]
print(result)
print('время выполнения 1: ', perf_counter() - start, sys.getsizeof(result))

start = perf_counter()
ex = src[0]
result = []
for el in src:
    if el > ex:
        result.append(el)
    ex = el
print(result)
print('время выполнения 2: ', perf_counter() - start, sys.getsizeof(result))

start = perf_counter()
ex = src[0]
result = set()
for el in src:
    if el > ex:
        result.add(el)
    ex = el
print(result)
print('время выполнения 3: ', perf_counter() - start, sys.getsizeof(result))