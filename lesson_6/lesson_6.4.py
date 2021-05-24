class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def move(self):
        return f'{self.name} has started'

    def stop(self):
        return f'{self.name} has stopped'

    def turn_right(self):
        return f'{self.name} has turned right'

    def turn_left(self):
        return f'{self.name} has turned left'

    def show_speed(self):
        return f'Current speed of {self.name} is {self.speed} mph'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of {self.name} is {self.speed} mph')

        if self.speed > 60:
            return f'Speed of {self.name} is above the allowable limit!'
        else:
            return f'Speed of {self.name} is within the limit'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of {self.name} is {self.speed} mph')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allowable limit for a work car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is a police vehicle'
        else:
            return f'{self.name} is not a police vehicle'


ferrari = SportCar(160, 'Red', 'Ferrari SF90', False)
toyota = TownCar(37, 'Black', 'Toyota Camry', False)
isuzu = WorkCar(82, 'White', 'Isuzu D-Nax pickup', True)
ford = PoliceCar(125, 'Blue',  'Ford Interceptor', True)

print(toyota.move())
print(toyota.show_speed())
print(f'When {toyota.turn_right()}, {isuzu.turn_left()}')
print(f'{isuzu.name} is {isuzu.color}')
print(f'Is {ferrari.name} a police vehicle? {ferrari.is_police}')
print(ferrari.show_speed())
print(ford.police())
print(ford.show_speed())
print(f'When {ford.move()}, {ferrari.stop()}')
