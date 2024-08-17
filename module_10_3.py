import threading
import random
from time import sleep


class Bank:
    lock = threading.Lock()
    def __init__(self):
        self.balance = 0

    def deposit(self, n=100):
        i = 0
        while i <= n:
            i += 1
            random_int = random.randint(50, 500)
            self.balance += random_int
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {random_int}. Баланс: {self.balance}')
            sleep(0.001)


    def take(self, m=100):
        j = 0
        while j <= m:
            j += 1
            random_int_1 = random.randint(50, 500)
            print(f'Запрос на снятие {random_int_1}')
            if random_int_1 <= self.balance:
                self.balance -= random_int_1
                print(f'Снятие: {random_int_1}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
