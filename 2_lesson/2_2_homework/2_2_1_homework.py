"""
За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?
Программа получает на вход числа n и m.
"""

n, m = int(input("Сколько километров проезжает машина за день?\n")), \
       int(input("Сколько километров проедет машина по маршруту?\n"))

cal_day = m // n
cal_hour = str((m / n) - (m // n)).split(".")[1][0]


if cal_day % 10 == 1 and cal_day % 100 != 11:
    day = "день"
elif 2 <= cal_day % 10 <= 4 and not 12 <= cal_day % 100 <= 14:
    day = "дня"
else:
    day = "дней"

if int(cal_hour) % 10 == 1:
    hour = "час"
elif 2 <= int(cal_hour) % 10 and not 5 <= int(cal_hour) % 100 <= 20:
    hour = "часа"
else:
    hour = "часов"


print(f"Требуется {cal_day} {day} и {cal_hour} {hour}, чтобы проехать маршрут длинной {m} километров.")
