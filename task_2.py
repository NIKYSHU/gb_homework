tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
def my_zip():
    for i, tutor in enumerate(tutors):
        if i < len(klasses):
            klass = klasses[i]
        else:
            klass = None
        yield (tutor, klass)
result = my_zip()
print(result)
print(next(result))
print(*result)
print(*my_zip())

result = ((a, b) for a, b in zip(tutors, klasses))
print(result)
print(*result)