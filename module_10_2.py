from threading import Thread
from time import sleep


class Knight(Thread): # класс наследуется от класса Thread
    def __init__(self, name, power): # конструктор класса
        super().__init__() # вызов
        self.name = name # атрибут класса Name
        self.power = power # атрибут класса Power

    def run(self): # метод run
        enemies = 100 # количество врагов изначально 100
        days = 0 # количество дней битвы
        print(f'{self.name} на нас напали!')
        for i in range(enemies): # цикл по количеству врагов
            if enemies > 0:
                enemies -= self.power # уменьшение количества врагов
                days += 1 # увеличивает количество дней битвы
                sleep(1) # задержка в 1 сек
                print(f'{self.name} сражается {days} дней(дня)..., осталось {enemies} воинов.')
            if enemies <= 0:
                print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились')
