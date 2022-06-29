# num_list = [1, 2, 3, 4, 5]
# str = 'dwadwadwa'
#
# for i in str:
#     print(i)
#
# print(dir(num_list))
# print(dir(str))
#

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#
#
# class SimpleIterator:
#     def __init__(self, limit):
#         self.limit = limit
#         self.counter = 0
#
#     def __next__(self):
#         if self.counter < self.limit:
#             self.counter += 1
#             return f'Add count... count is {self.counter}'
#         else:
#             raise StopIteration
#
#
# s_iter1 = SimpleIterator(3)
#
# print(next(s_iter1))
#
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 
# class SimpleIterator:
#     def __iter__(self):
#         return self
# 
#     def __init__(self, limit):
#         self.limit = limit
#         self.counter = 0
# 
#     def __next__(self):
#         if self.counter < self.limit:
#             self.counter += 1
#             return self.counter
#         else:
#             raise StopIteration
# 
# 
# s_inter2 = SimpleIterator(5)
# 
# for i in s_inter2:
#     print(i)
# 
# print(next(s_inter2))
#
# num_list = [1, 2, 3, 4, 5]
# iter = iter(num_list)
# print(next(iter))
# print(next(iter))
# print(next(iter))
# print(next(iter))
# print(next(iter))
# print(next(iter))


