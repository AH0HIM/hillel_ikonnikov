"""
3. Напишите программу Python для построения следующего шаблона, используя вложенный цикл for.

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

"""
line = 9

for i in range(line + 1):
    for j in range(i):
        if i + j <= line:
            print("*", end=" ")
    print()
