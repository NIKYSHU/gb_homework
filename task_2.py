def type_logger(func):
    def inner(*args):
        rezult = func(*args)
        for item in args:
            print(f'{func.__name__}({item}: {type(item)})')
        return rezult
    return inner

@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)