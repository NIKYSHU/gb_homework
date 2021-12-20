class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'start drawing with {self.title}.')


class Pen(Stationery):
    def draw(self):
        print(f'start drawing with {self.title}.')


class Pencil(Stationery):
    def draw(self):
        print(f'start drawing with {self.title}.')


class Handle(Stationery):
    def draw(self):
        print(f'start drawing with {self.title}.')


S = Stationery('stationery')
P = Pen('pen')
PL = Pencil('pencil')
H = Handle('hendle')

S.draw()
P.draw()
PL.draw()
H.draw()