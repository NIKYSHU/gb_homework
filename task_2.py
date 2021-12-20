class Road:
    __length = 5000
    __width = 20
    def mass_asphalt(self, length=__length, width=__width):
        mass = ((length * width * 25 * 5) / 1000)
        return mass
R = Road()
print((R.mass_asphalt(length=1000, width=6)), 'тонн')