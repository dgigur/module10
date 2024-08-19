from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        counter = 0
        while len(file.readline()) != 0:
            counter += 1
            all_data.append(file.readline())
        else:
            print(f"Строка {counter+1} пустая")


filenames = [f'./file {number}.txt' for number in range(1, 5)]

"""start = datetime.now()
for _ in filenames:
    read_info(_)
end = datetime.now()
print(end - start)"""
# 0:00:03.076691

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        start_1 = datetime.now()
        pool.map(read_info, filenames)
    end_1 = datetime.now()
    print(end_1 - start_1)

# 0:00:01.144283