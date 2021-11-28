rus_words = {
    'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
    'six': 'шесть', 'seven': 'семь', 'eighth': 'восемь', 'nine': 'девять', 'ten': 'десять'
}
def num_translate(word):
    print(rus_words.get(word, 'None'))
num_translate(input('введите число (англ.) - '))
