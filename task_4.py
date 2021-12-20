class Car:
    def __init__(self, speed, color, name, direction, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.direction = direction
        self.is_police = is_police

    def is_polizei(self):
        self.is_police = False
        return self.is_police

    def go(self):
        print('we ride')

    def turn(self):
        if self.direction == 'l':
            print('we turning left')
        elif self.direction == 'r':
            print('we turning right')
        elif self.direction == 's':
            print('we go straight')
        else:
            print('I can not do that')

    def stop(self):
        print('we stop')

    def show_speed(self):
        print(f'our speed is: {self.speed}')

    def show_all(self):
        self.go()
        self.show_speed()
        self.turn()
        print(f'color is: {self.color}')
        print(f'police: {self.is_polizei()}')
        print(f'name is: {self.name}')


class TownCar(Car):
    def show_speed(self):
        print(f'our speed is: {self.speed}')
        if self.speed > 60:
            print('warning! high speed!')


class SportCar(Car):
    def show_speed(self):
        print(f'our speed is: {self.speed}')
        if self.speed < 40:
            print('warning! too slow!')


class WorkCar(Car):
    def show_speed(self):
        print(f'our speed is: {self.speed}')
        if self.speed > 40:
            print('warning! high speed!')


class PoliceCar(Car):
    def is_polizei(self):
        self.is_police = True
        return self.is_police


C = PoliceCar(speed=66, color='police color', direction='r', name='mahoney')
C.show_all()