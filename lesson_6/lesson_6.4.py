class Cars:
    name = None
    speed = None
    color = None
    is_police = False

    def __init__(self, name, speed, color, is_police = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
    def go(self):
        return "The car went"
    def stop(self):
        return "The car has stopped"
    def turn(self, direction):
        return "The car turned to " + direction

class TownCar(Cars):
    family = None
    def __init__(self, name, speed, color, family = True):
        super().__init__(name, speed, color)
        self.family = family

class SportCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)

class WorkCar(Cars):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

class PoliceCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)

ford = TownCar('Ford', 60, 'black')
print(ford.name, ford.color, ford.speed, ford.is_police)
print(ford.go(), ford.turn('City'), ford.stop())
sport = SportCar('Ford', 180, 'red')
work1 = WorkCar('Ford', 90, 'white', True)
work2 = WorkCar('Audi', 90, 'white', False)
police = PoliceCar('Ford', 180, 'red')

_______________________________________________________________________________________

class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Speed of {self.name} is normal for town car'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'


audi = SportCar(100, 'Red', 'Audi', False)
oka = TownCar(30, 'White', 'Oka', False)
lada = WorkCar(70, 'Rose', 'Lada', True)
ford = PoliceCar(110, 'Blue',  'Ford', True)
print(lada.turn_left())
print(f'When {oka.turn_right()}, then {audi.stop()}')
print(f'{lada.go()} with speed exactly {lada.show_speed()}')
print(f'{lada.name} is {lada.color}')
print(f'Is {audi.name} a police car? {audi.is_police}')
print(f'Is {lada.name}  a police car? {lada.is_police}')
print(audi.show_speed())
print(oka.show_speed())
print(ford.police())
print(ford.show_speed())
