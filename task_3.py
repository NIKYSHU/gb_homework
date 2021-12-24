from uuid import uuid4

class Cell:
    @staticmethod
    def make_order(cell_class, cell_units):
        """
            Генерация вывода клетки.
            :param cell_class: Класс "Клетка"
            :param cell_units: Количество/размер ряда.
            :return: Вернет заполненные ряды в количестве ячеек, которые занимает клетка.
        """
        if type(cell_class) == Cell:
            s = ''
            for i in range(0, cell_class.squares):
                if i % cell_units == 0 and i > 0:
                    s = s + chr(13) + chr(10)
                s = s + '*'
            return s
        else:
            raise Exception('Некорректного использование метода!')

    def __init__(self, squares):
        self.__id = uuid4()
        try:
            self.__squares = int(squares)
            if self.__squares <= 0:
                self.__squares = 1  # Клетка не может ничего не занимать.
        except:
            raise Exception('Клетка должна занимать минимум 1 ячейку (int)')

    @property
    def squares(self):
        return self.__squares

    @property
    def id(self):
        return self.__id

    def __str__(self):
        return f'Клетка {self.__id}, имеет размер: {self.squares} ячеек.'

    def __sub__(self, other):
        if type(other) == Cell:
            ret = self.squares - other.squares
            if ret <= 0:
                raise Exception('Нельзя исчерпать клетку до дна.')
            else:
                return Cell(ret)
        else:
            raise Exception('Из клетки можно вычитать только другую клетку.')

    def __add__(self, other):
        if type(other) == Cell:
            return Cell(self.squares + other.squares)
        else:
            raise Exception('Клетку можно складывать только с другой клеткой.')

    def __mul__(self, other):
        if type(other) == Cell:
            return Cell(self.squares * other.squares)
        else:
            raise Exception('Клетку можно перемножать только с другой клеткой.')

    def __floordiv__(self, other):
        if type(other) == Cell:
            ret = self.squares // other.squares
            if ret <= 0:
                raise Exception('Деление невозможно, так как клетка будет уничтожена.')
            else:
                return Cell(ret)
        else:
            raise Exception('Клетку можно делить только на другую клетку.')

    def __truediv__(self, other):
        if type(other) == Cell:
            ret = self.squares % other.squares
            if ret <= 0:
                raise Exception('Деление невозможно, так как клетка будет уничтожена.')
            else:
                return Cell(ret)
        else:
            raise Exception('Клетку можно делить только на другую клетку.')

c1 = Cell(5)
print(c1)
c2 = Cell(2)
print(c2)
c3 = c1 + c2
print(c3)
c4 = c1 - c2
print(c4)
c5 = c1 * c3
print(c5)
c6 = c1 / c4
print(c6)
c7 = c1 // c4
print(c7)

print(Cell.make_order(c5, 3))