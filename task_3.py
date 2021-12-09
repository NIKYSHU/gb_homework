from sys import argv
with open("bakery.csv", "r", encoding="utf-8") as bagle_r:
    if 1 < len(argv) < 4 and [i for i in argv[1:] if i.isdigit()]:
        if len(argv) == 3:
            start, finish = map(int, argv[1:])
            print(*(v for i, v in enumerate(bagle_r) if start - 1<= i < finish), sep="")
        else:
            print(*(v for i, v in enumerate(bagle_r) if i >= int(argv[1]) -1), sep="")
    else:
        print(bagle_r.read())

from sys import argv
with open("bakery.csv", "a", encoding="utf-8") as bagle_a:
    with open("bakery.csv", "r", encoding="utf-8") as bagle_r:
        if len(argv) > 1 and [i for i in argv[1:] if "." in i and i.replace(".", "").isdigit()]:
            if round(float(argv[1]), 3) <=99999.99:
                print(f'{round(float(argv[1]), 3):>010}', file=bagle_a)
            else:
                print("number must be less than 99 999,999")
        else:
            print(bagle_r.read())
