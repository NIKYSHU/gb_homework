import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
def get_joke(not_repeat):
    """ функция возвращает случайно сгенерированные шутки по спискам, имеет возможность контроля уникальности """
    if not_repeat and (len(nouns) == 0 or len(adverbs) == 0 or len(adjectives) == 0):
        return ' -/-/-'
    noun = random.choice(nouns)
    adverb = random.choice(adverbs)
    adjective = random.choice(adjectives)
    if not_repeat:
        adjectives.remove(adjective)
        nouns.remove(noun)
        adverbs.remove(adverb)
    return f'{noun} {adverb} {adjective}'
def get_jokes(num=1, not_repeat=False):
    global nouns
    global adverbs
    global adjectives
    list_word = [nouns[:], adverbs[:], adjectives[:]]
    list_jokes = []
    for i in range(num):
        list_jokes.append(get_joke(not_repeat))
    print(list_jokes)
    nouns = list_word[0]
    adverbs = list_word[1]
    adjectives = list_word[2]
get_jokes(num=5)
get_jokes(not_repeat=True, num=5)
get_jokes(6, True)
get_jokes(4)