import threading
import random
from time import sleep


class Bank:
    lock = threading.Lock()

    def __init__(self):
        self.balance = 0
        self.i, self.j = 0, 0
        self.n = 100

    def deposit(self):
        while self.i <= self.n:
            #print(f'i={self.i}')
            self.i += 1
            random_int = random.randint(50, 500)
            self.balance += random_int
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            elif self.i > self.n and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {random_int}. Баланс: {self.balance}')
            sleep(0.001)

    # Поток пополнений у нас непрерывный так как нет команды на закрытие замка. Но мы высталвили задержку 0.001
    # после каждого пополнения

    def take(self):
        while self.j <= self.n:
            #print(f'j={self.j}')
            if self.lock.locked() and self.i < 100:
                self.lock.acquire()
                self.lock.release()
            # Если ввести задержку у потока снятий, то может получиться, что деньги закончатся раньше чем количество снятий.
            # Следующее условие нужно чтобы 2 поток мог разблокировать сам себя и закончить все итерации.
            elif self.lock.locked() and self.i >= 100:
                self.lock.release()
            self.j += 1
            random_int_1 = random.randint(50, 500)
            print(f'Запрос на снятие {random_int_1}')
            if random_int_1 <= self.balance:
                self.balance -= random_int_1
                print(f'Снятие: {random_int_1}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            #sleep(0.002)


# Поток снятий у нас прерываемый только в том случае если произойдет нехватка средств для снятия.
# Если средств у нас будет не хватать, то поток закрывает замок, но, чтобы остановиться, ему нужно вновь
# дойти до замка, чтобы остановиться (а это 1 пустая итерация). Для исключения этой пустой итерации
# можно ввести в начало условие: при закрытом замке мы вновь пытаемся его закрыть(что останавливает поток в
# начале итерации) тем самым 2 поток будет ждать пока первый поток открывает замок, затем второй поток его вновь закроет
# и тут же откроет, чтобы никому не мешать.
# При всем этом операция снятия может произойти несколько раз, если для этого хватает баланса, прежде
# чем произойдет пополнение, так как снятие происходит без задержек. Из-за этого 100 операций снятия закончатся
# раньше чем 100 операций пополнения. К тому же периодически происходит итерация при которой не хватает
# баланса для снятия. Счетчик уменьшается, но баланс при этом нет.


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
