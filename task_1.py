import time
class TrafficLight:
    __color = 'yellow', 'green', 'red'

    def running(self, c, t, color=__color):
        if c in color:
            print(c)
            time.sleep(t)
T = TrafficLight()
T.running('red', 7)
T.running('yellow', 2)
T.running('green', 5)
