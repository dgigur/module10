from threading import Thread
from time import sleep
class Knight(Thread):
    enemies = 100
    day_count = 0
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemies > 0:
            self.enemies -= self.power
            self.day_count += 1
            print(f'{self.name} сражается {self.day_count} дней, осталось {self.enemies} воинов.\n')
            sleep(1)
        print(f'{self.name} одержал победу спустя {self.day_count} дней(дня)!\n')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
