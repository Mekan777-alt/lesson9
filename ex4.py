"""Реализуйте базовый класс Car:
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
"""
from random import randint, choice

class Car:
    is_police = False
    'Родительский класс'
    def __init__(self, speed: int, color: str, name: str):
        self.speed = speed
        self.color = color
        self.name = name

    def show_speed(self):
        return f'Начальная скорость автомобиля {self.name} равна {self.speed}'

    def go(self):
        self.speed = randint(20, 80)
        return f'Машина {self.name} двинулась'

    def stop(self):
        self.speed = 0
        return f'Машина марки {self.name} остановилась'

    def turn(self, direction: str):
        return f'Машина {self.name} повернула {direction}'



class TownCar(Car):
    'Дочерний класс'
    is_police = False
    def speed_town_car(self):
        alarm = '. Внимание снизти скорость!' if self.speed > 40 else "."
        return f'Скорость автомобиля {self.name} равна: {self.speed}{alarm}'

class SportCar(Car):
    'Дочерний класс'
    is_police = False

class WorkCar(Car):
    'Дочерний класс'
    is_police = False
    def speed_work_car(self):
        alarm = '. Внимание! Превышение скорости!' if self.speed > 60 else '.'
        return f'Скорость автомобиля {self.name} равна: {self.speed}{alarm}'

class PoliceCar(Car):
    'Дочерний класс'
    is_police = True

t_car = TownCar(0, 'red', 'Mazda')
s_car = SportCar(0, 'blue', 'Ferrari')
w_car = WorkCar(0, 'yellow', 'Kia')
p_car = PoliceCar(0, 'blue','Lexus')
car_list = [t_car, s_car, w_car, p_car]

for car in car_list:
    print(f'\n{car.speed}', end=', ')
    print(car.color, end=', ')
    print(car.name, end=', ')
    print(car.is_police)
    print(car.go())
    print(car.turn(choice(('направо', 'налево'))))
    print(car.show_speed())
    print(car.stop())