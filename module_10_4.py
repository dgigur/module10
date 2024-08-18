from threading import Thread
from random import randint
from time import sleep
import queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep_number = randint(3, 10)
        sleep(sleep_number)


class Cafe:
    def __init__(self, *args):
        tables = []
        for i in args:
            tables.append(i)
        self.queue = queue.Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        counter = 0
        for i in guests:
            counter += 1
            for j in self.tables:
                if j.guest is None:
                    j.guest = i
                    i.start()
                    print(f'{i.name} сел(-а) за стол номер {j.number}')
                    break
                elif counter > len(self.tables):
                    self.queue.put(i)
                    print(f'{i.name} в очереди')
                    break

    def discuss_guests(self):
        while not self.queue.empty() or any([x.guest != None for x in self.tables]):
            for i in self.tables:
                if i.guest is not None and not i.guest.is_alive():
                    print(f'{i.guest.name} покушал(-а) и ушёл(ушла)\nСтол номер {i.number} свободен')
                    i.guest = None
                elif not self.queue.empty() and i.guest is None:
                    i.guest = self.queue.get()
                    print(f'{i.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {i.number}')
                    i.guest.start()
                else:
                    continue


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
