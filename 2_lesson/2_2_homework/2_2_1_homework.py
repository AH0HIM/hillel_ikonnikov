"""
За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?
Программа получает на вход числа n и m.
"""

n, m = float(input("Сколько километров проезжает машина за день?\n")), \
       float(input("Сколько километров проедет машина по маршруту?\n"))

cal_day = m // n
cal_hour = str((m / n) - (m // n)).split(".")[1][0]
cal_meters = str(m - int(m)).split(".")[1][0]


def get_day():
    if cal_day % 10 == 1 and cal_day % 100 != 11:
        return "день"
    elif 2 <= cal_day % 10 <= 4 and not 12 <= cal_day % 100 <= 14:
        return "дня"
    else:
        return "дней"


def get_hour():
    if int(cal_hour) % 10 == 1:
        return "час"
    elif 2 <= int(cal_hour) % 10 and not 5 <= int(cal_hour) % 100 <= 20:
        return "часа"
    else:
        return "часов"


def get_kilometer():
    if int(m) % 10 == 1:
        return "километр"
    elif 2 <= int(m) % 10 and not 5 <= int(m) % 100 <= 20:
        return "километра"
    else:
        return "километров"


def get_meter():
    if int(cal_meters) % 10 == 1:
        return "метр"
    elif 2 <= int(cal_meters) % 10 and not 5 <= int(cal_meters) % 100 <= 20:
        return "метра"
    else:
        return "метров"


print(f"Требуется {int(cal_day)} {get_day()} и {cal_hour} {get_hour()}, "
      f"чтобы проехать маршрут длинной {int(m)} {get_kilometer()} и {cal_meters} {get_meter()}.")
