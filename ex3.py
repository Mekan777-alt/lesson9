"""
Реализовать базовый класс Worker (работник):
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

"""

class Worker:
    '''Родительский класс'''
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income

    def get_params(self):
        """Запросить все атрибуты"""
        return self.name, self.surname, self.position, self._income

class Position(Worker):
    '''Дочерний класс'''
    def get_full_name(self):
        '''Метод возврата полного имени'''
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        '''Метод расчета зароботной платы'''
        return self._income['wage'] + self._income['bonus']


workers = list()
positions = list()

workers.append(Worker('Медедов', 'Мекан', 'Инженер', {'wage': 15000, 'bonus': 500}))
workers.append(Worker('Петров', 'Иван', 'Преподователь', {'wage': 4000, 'bonus': 200}))
workers.append(Worker('Уткин', 'Василий', 'Бухгалтер', {'wage': 10000, 'bonus': 700}))
workers.append(Worker('Ларионов', 'Николай', 'Руководитель', {'wage': 7000, 'bonus': 900}))

for worker in workers:
    positions.append(Position(*worker.get_params()))

for posit in positions:
    print(f'\nДанные по работнику:\t{posit.get_params()}')
    print(f'Полное имя работника:\t{posit.get_full_name()}')
    print(f'Полный доход работника:\t{posit.get_total_income()}')