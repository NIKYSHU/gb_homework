print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))
# или так
var_list = ['15 * 2', '15 / 3', '15 // 2', '15 ** 2']
for i in var_list:
    print(f"тип выражения '{i}' - {type(eval(i))}")