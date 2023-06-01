class Car:
    engine = None
    wheels = None
    doors = None
    color = None

    def horn(self):
        print("pibip")

    def __repr__(self):
        values = f"{self.__class__.__name__} {self.engine=} {self.wheels=} {self.doors=} {self.color=}"
        return values

    def __str__(self):
        values = f"{self.engine=} {self.wheels=} {self.doors=} {self.color=}"
        return values


class Mercedes(Car):
    engine = "japan"
    wheels = "20"
    doors = "aluminium"

    def horn(self):
        print("pibip x3")


class Ford(Car):
    engine = "germany"
    wheels = "19"
    doors = "metal"


class Galaxy(Ford):
    color = "black"

    def horn(self):
        print("pibip pibip")


class HandMade(Mercedes, Galaxy):
    ...


galaxy = Galaxy()
print(galaxy)
galaxy.color = 'red'
galaxy.wheels = '21'
print(galaxy)
breakpoint()
print(repr(galaxy))

e80 = Mercedes()
print(e80)
e80.color = 'red'
e80.wheels = '21'
e80.my_wheel = e80.color + e80.wheels
print(e80)


hand_made = HandMade()
hand_made.horn()