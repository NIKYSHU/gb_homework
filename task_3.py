some_people = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for el in some_people:
    print(f'Привет, {el.split(" ")[len(el.split(" ")) - 1].capitalize()}!')