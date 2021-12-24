from abc import ABC, abstractmethod

class Cloth(ABC):
    __cl_data = {0: 'Неизвестно', 1: 'Костюм', 2: 'Пальто'}

    @abstractmethod
    def __init__(self):
        self.__cloth_type = self.__cl_data.get(0)
        self.__measure = 0

    @property
    def cloth_type(self):
        return self.__cloth_type

    @cloth_type.setter
    def cloth_type(self, value):
        self.__cloth_type = self.__cl_data.get(value, 0)
        self.measure = 1

    @property
    def measure(self):
        return self.__measure

    @measure.setter
    def measure(self, value):
        self.__measure = value

    @property
    def material_count(self):
        if self.__cloth_type == self.__cl_data.get(1, 0):
            return 2 * self.measure + 0.3
        elif self.__cloth_type == self.__cl_data.get(2, 0):
            return self.measure / 6.5 + 0.5
        else:
            return 0

    def __str__(self):
        return f'Одежда: {self.cloth_type}, размер: {self.measure}. Требуется материала: {self.material_count} м.'

class MySuit(Cloth):
    def __init__(self):
        super().__init__()
        self.cloth_type = 1

class MyCoat(Cloth):
    def __init__(self):
        super().__init__()
        self.cloth_type = 2


suit = MySuit()
suit.measure = 10
print(suit)


coat = MyCoat()
coat.measure = 45
print(coat)