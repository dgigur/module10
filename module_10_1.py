from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count+1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


time_start_1 = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end_1 = datetime.now()
time_res_1 = time_end_1 - time_start_1
print(time_res_1)

time_start_2 = datetime.now()
first_trh = Thread(target=write_words, args=(10, 'example5.txt'))
second_trh = Thread(target=write_words, args=(30, 'example6.txt'))
third_thr = Thread(target=write_words, args=(200, 'example7.txt'))
fourth_thr = Thread(target=write_words, args=(100, 'example8.txt'))

first_trh.start()
second_trh.start()
third_thr.start()
fourth_thr.start()

first_trh.join()
second_trh.join()
third_thr.join()
fourth_thr.join()

time_end_2 = datetime.now()
time_res_2 = time_end_2 - time_start_2
print(time_res_2)
