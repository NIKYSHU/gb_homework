class ValueInvalidError(Exception):
    def __init__(self, message="Ошибка значения"):
        self.message = message
        super().__init__(self.message)


my_list = []

while True:
    try:
        i_num = input("Введите число (Целое, Дробное через '.', для завершения введите 'stop'): ")
        if i_num == 'stop':
            break
        try:
            my_list.append(int(i_num))
        except:
            try:
                my_list.append(float(i_num))
            except:
                raise ValueInvalidError
    except ValueInvalidError:
        print("Можно вводить только числа!\n")

print(','.join([str(x) for x in my_list]))