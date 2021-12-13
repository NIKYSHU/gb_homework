import os

some_data = r'C:/Users/nikys/PycharmProjects/gb_homework/some_data'
some = {}


def sizes(size1, size2):
    count = 0
    for i in os.scandir(some_data):
        if size1 < i.stat().st_size < size2:
            count += 1
            some[size2] = count
        else:
            some[size2] = count

sizes(0, 100)
sizes(100, 1000)
sizes(1000, 10000)
sizes(10000, 100000)
print(some)