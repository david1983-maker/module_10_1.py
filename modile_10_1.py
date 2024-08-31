import time
from time import sleep
from datetime import datetime
from threading import Thread

time_start = datetime.now()


def wite_words(word_count, file_name):
    count = 1
    file = open(file_name, 'w', encoding='utf-8')
    while count != word_count + 1:
        file.write(f'Какое то слово № {count}\n')
        count += 1
        time.sleep(0.1)

    print(f"Завершилась запись в файл {file_name}")


n1 = wite_words(10, 'example1.txt')
n2 = wite_words(30, 'example2.txt')
n3 = wite_words(200, 'example3.txt')
n4 = wite_words(100, 'example4.txt')
time_end = datetime.now()
time_res = time_end - time_start
print(time_res)

n5 = Thread(target=wite_words(10, 'example5.txt'))
n6 = Thread(target=wite_words(30, 'example6.txt'))
n7 = Thread(target=wite_words(200, 'example7.txt'))
n8 = Thread(target=wite_words(100, 'example8.txt'))

n5.start()
n6.start()
n7.start()
n8.start()

n5.join()
n6.join()
n7.join()
n8.join()
time_end = datetime.now()
time_res = time_end - time_start
print(time_res)
