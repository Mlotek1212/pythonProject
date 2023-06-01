class Kelvin:
    def __get__(self, cls, owner):
        return round(cls._absolute_temperature, 2)

    def __set__(self, cls, value):
        if value < 0:
            raise ValueError("...")
        cls._absolute_temperature = value


class Celsius:
    def __get__(self, cls, *args):
        value = cls._absolute_temperature - 273.15
        return round(value, 2)

    def __set__(self, cls, value):
        cls._absolute_temperature = value + 273.15


class CelsiusExternal:
    def __init__(self, *args, **kwargs):
        self.value = 0

    def __get__(self, cls, *args):
        return round(self.value, 2)

    def __set__(self, cls, value):
        self.value = value


class CelsiusExternal:
    def __init__(self, *args, **kwargs):
        self.value = 0

    def __get__(self, cls, *args):
        return round(self.value, 2)

    def __set__(self, cls, value):
        self.value = value


class Fahrenheit:
    def __get__(self, cls, *args):
        breakpoint()
        value = (cls._absolute_temperature - 273.15) * 9 / 5 + 32
        return round(value, 2)

    def __set__(self, cls, fahrenheit):
        cls._absolute_temperature = (fahrenheit - 32) * 5 / 9 + 273.15


class Temperature:
    kelvin = Kelvin()
    celsius = Celsius()
    celsius2 = CelsiusExternal(123, 234, instane='123', is_kelvin=False)
    fahrenheit = Fahrenheit()

    def __init__(self):
        self._absolute_temperature = 0.0


temp = Temperature()

breakpoint()
