# Генераторы - это функции, которые производят или выдает последовательность значений, используя ключевое слово yield
# Генераторы - это итераторы, по которым можно итерировать только один раз

# def simple_generator(val):
#     while val > 0:
#         val -= 1
#         yield val
#
#
# gen_iter = simple_generator(3)
# print(next(gen_iter))
# print(next(gen_iter))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def foo():
    print("begin")
    for i in range(35555):
        print("before yield", i)
        yield i
        print("after yield", i)
    print("end")


f = foo()
for i in f:
    print(i)
