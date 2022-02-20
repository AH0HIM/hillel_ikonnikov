"""
Вам дан код сортировки пузырьком, однако он работает неверно, там допущена ошибка. Используя дебагер, найдите и
исправьте ошибку. Опишите в комментарии к коду, в чем была ошибка. Добавьте минимум 5 тестов для этого кода
"""


def bubble_sort(l):
    t = l.copy()

    # for n in range(0, len(t)):            # лишний внешний цикл
    #     for i in range(len(t) - n):       # лишний последний елемент
    #         if t[i] > t[n]:               # неправильный индекс правого соседнего элемента
    #             t[i], t[n] = t[n], t[i]   # неправильная перестановка соседнего элементов
    for n in range(0, len(t) - 1):
        for i in range(len(t) - n - 1):
            if t[i] > t[i + 1]:
                t[i], t[i + 1] = t[i + 1], t[i]

    return t


nums = [4, 1, 6, 3, 2, 7, 8]
sorted = bubble_sort(nums)
print(sorted)


# Test stage

actual_result = bubble_sort([17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, 96, -98, 56, 92, 1, 32])
expected_result = [-98, -71, -71, -27, -16, 1, 17, 24, 32, 48, 56, 58, 67, 79, 88, 88, 91, 92, 96, 96]
assert actual_result == expected_result

actual_result = bubble_sort([0, 0, 0, 0, 0])
expected_result = [0, 0, 0, 0, 0]
assert actual_result == expected_result

actual_result = bubble_sort([])
expected_result = []
assert actual_result == expected_result

actual_result = bubble_sort([99, 1, 100, 1, 2, -99])
expected_result = [-99, 1, 1, 2, 99, 100]
assert actual_result == expected_result

actual_result = bubble_sort([100, -100])
expected_result = [-100, 100]
assert actual_result == expected_result
