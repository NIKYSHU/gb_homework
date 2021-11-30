def thesaurus(*args):
    name_list = {}
    for name in args:
        if name[0] in name_list.keys():
            name_list[name[0]].append(name)
        else:
            name_list[name[0]] = [name]

    print(name_list)
thesaurus("Иван", "Мария", "Сергей", "Петр", "Илья", "Игорь")
list_name = ['Иван', 'Игоррь', 'Илья', 'Дима', 'Михаил']
list_name.sort()
thesaurus(*list_name)
