"""
За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?
Программа получает на вход числа n и m.
"""


def get_start():
    n, m = float(input("Сколько километров проезжает машина за день?\n")), \
           float(input("Сколько километров проедет машина по маршруту?\n"))
    return get_cal(n, m)


def get_cal(n, m):
    cal_day = m // n
    cal_hour = str((m / n) - (m // n)).split(".")[1][0]
    cal_meters = str(m - int(m)).split(".")[1][0]
    return get_print(get_day(cal_day), get_hour(cal_hour), get_kilometer(m), get_meter(cal_meters),
                     cal_day, cal_hour, m, cal_meters)


def get_day(cal_day):
    if cal_day % 10 == 1 and cal_day % 100 != 11:
        return "день"
    elif 2 <= cal_day % 10 <= 4 and not 12 <= cal_day % 100 <= 14:
        return "дня"
    else:
        return "дней"


def get_hour(cal_hour):
    if int(cal_hour) % 10 == 1:
        return "час"
    elif 2 <= int(cal_hour) % 10 and not 5 <= int(cal_hour) % 100 <= 20:
        return "часа"
    else:
        return "часов"


def get_kilometer(m):
    if int(m) % 10 == 1:
        return "километр"
    elif 2 <= int(m) % 10 and not 5 <= int(m) % 100 <= 20:
        return "километра"
    else:
        return "километров"


def get_meter(cal_meters):
    if int(cal_meters) % 10 == 1:
        return "метр"
    elif 2 <= int(cal_meters) % 10 and not 5 <= int(cal_meters) % 100 <= 20:
        return "метра"
    else:
        return "метров"


def get_print(day, hour, kilometer, meters, cal_day, cal_hour, cal_kilometer, cal_meters):
    print(f"Требуется {int(cal_day)} {day} и {cal_hour} {hour}, "
          f"чтобы проехать маршрут длинной {int(cal_kilometer)} {kilometer} и {cal_meters} {meters}.")


get_start()