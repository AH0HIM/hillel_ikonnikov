# generator.py
# A list of tasks to run
from collections import deque


def countdown_task(n):
    while n > 0:
        print(n)
        x = yield n
        print(f"{countdown_task.__name__} received: {x}")
        n -= 1

def countup_task(n):
    while n < 10:
        print(n)
        yield n
        n += 1

tasks = deque([countdown_task(5),
               countdown_task(10),
               countup_task(-5)])


def scheduler(tasks):
    while tasks:
        task = tasks.popleft()
        try:
            y = next(task)  # Run to the next yield
            print(f"---: {y}")
            task.send(y + 1)
            tasks.append(task)  # Reschedule
        except StopIteration:
            print(task)


# Run it
scheduler(tasks)
