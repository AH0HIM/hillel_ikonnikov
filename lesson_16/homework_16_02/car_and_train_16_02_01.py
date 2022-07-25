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

CAR_SPEED = random.randrange(30, 170)
TRAIN_SPEED = random.randrange(70, 110)
CROSSROADS = 20
DISTANCE = 0


def car_run(th):
    global DISTANCE
    for i in range(0, 10):
        DISTANCE += round(CAR_SPEED * (i / 60), 1)
        print(f'{threading.current_thread().name} '
              f'speed: {CAR_SPEED} km/h, '
              f'distance: {DISTANCE} m')
        time.sleep(1)
        if DISTANCE >= CROSSROADS:
            th.join()

    print('Car finish')


def train_run():
    global DISTANCE
    for i in range(0, 10):
        DISTANCE += round(TRAIN_SPEED * (i / 60), 1)
        print(f'{threading.current_thread().name} '
              f'speed: {TRAIN_SPEED} km/h, '
              f'distance: {DISTANCE} m')
        time.sleep(1)

    print('Train finish')


th_train = Thread(target=train_run, name='Train')
th_car = Thread(target=car_run, args=(th_train, ), name='Car')


th_car.start()
th_train.start()
