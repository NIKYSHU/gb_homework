duration = int(input('Введите длительность в секундах :  '))
days = duration // 86400
hours = (duration // 3600) % 24
minutes = (duration // 60) % 60
seconds = duration % 60
print(days, 'дн--', hours, 'час--', minutes, 'мин--', seconds, 'сек--')