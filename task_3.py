class Worker:
    # name = None
    # surname = None
    # position = None
    # _income = {"wage": None, "bonus": None}

    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income

class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        total = self._income.get('wage') + self._income.get('bonus')
        print(total)

P = Position('ivan', 'petrov', 'slave', ({'wage': 500, 'bonus': 100}))
P.get_full_name()
P.get_total_income()
S = Position('stas', 'petrov', 'his_slave', ({'wage': 666, 'bonus': 333}))
S.get_full_name()
S.get_total_income()