"""
Потрібно створити 2 додаткові потоки з назвою авто та потяг. Ці потоки перетинатися в певній ділянці шляху - crossroads
(global). Потік авто має певну швидкість від 30 до 170km/h. Потік потяг має швидкість від 70-110km/h. (random.range)

Необхідно змоделювати рух обох потоків так, щоб вони рушили з однієї й тієї ж точки. Рухались упродовж певного часу
(наприклад 10 секунд) і могли перетинатися в точці crossroads.

Якщо авто має вищу швидкість ніж потяг та обганяє потяг до точки перетину на 20 метрів то воно не чекає потік - потяг.
Якщо авто, не має не встигати на ці 20 метрів, то воно має почекати закінчення потоку - потяга (довжина потоку потяга 5
секунд) і лише після цього продовжити свій рух без обмеження в часі.
"""

import random
import threading
import time
from threading import Thread

car_speed = random.randrange(30, 170)
train_speed = random.randrange(70, 110)
crossroads = 0


def car_run(th):
    global crossroads
    distance = 0
    for i in range(0, 10):
        crossroads += 1
        distance += round(car_speed * (i / 60), 1)
        print(f'{threading.current_thread().name} '
              f'speed: {car_speed} km/h, '
              f'distance: {distance} m')
        time.sleep(1)
        if distance >= crossroads:
            th.join()

    print('Car finish')


def train_run():
    distance = 0
    for i in range(0, 10):
        distance += round(train_speed * (i / 60), 1)
        print(f'{threading.current_thread().name} '
              f'speed: {train_speed} km/h, '
              f'distance: {distance} m')
        time.sleep(1)

    print('Train finish')


th_train = Thread(target=train_run, name='Train')
th_car = Thread(target=car_run, args=(th_train, ), name='Car')


th_car.start()
th_train.start()
