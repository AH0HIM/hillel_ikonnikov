from .employee import Employee
import time
import pytest
import logging
# from flaky import flaky
import random


# class TestPerson:
#
#     @pytest.mark.smoke
#     def test_email(self):
#         logging.info("TestPerson")
#         emp1 = Employee('Sergii', 'T', 5000)
#         assert "sergii.t@email.com.ua" == emp1.email
#         print("Test Pass")
#
#     def test_email2(self):
#         emp1 = Employee('Sergi', 'T', 5000)
#         assert "sergii.t@email.com.ua" == emp1.email
#         print("Test Pass")
#
#     def test_class_apply_raise(self):
#         emp1 = Employee('Sergii', 'T', 5000)
#         emp1.apply_raise()
#         # time.sleep(5)
#         assert emp1.pay == 5000 * 1.05


# @flaky(max_runs=20, min_passes=2)
# def test_apply_raise():
#     emp1 = Employee('Sergii', 'T', 5000)
#     emp1.apply_raise()
#     time.sleep(1)
#     assert emp1.pay == 5000 * random.choice([1.05, 1.1])

@pytest.mark.parametrize("x, y, expected_result",
                         [(10, 10, 20),
                          (-10, 10, 0),
                          (0, -10, -10),
                          (-15, -1, -16),
                          (-15.5, -1.0, -16.5),
                          # pytest.param("15", 1, pytest.raises(AssertionError), marks=[pytest.mark.xfail])
                          ])
def test_sum(x, y, expected_result):
    assert sum((x, y)) == expected_result


# test_sum(10, 10, 20)
# test_sum(-10, 10, 0)
# test_sum(0, -10, -10)
# test_sum(-15, -1, -16)
# test_sum(-15.5, -1.0, -16.5)


# test_sum("-15.5", -1.0, TypeError)

#
# def test_sum1():
#     x = 10
#     assert sum((x, 10)) == 20
#
#
# def test_sum2():
#     x = -10
#     assert sum((x, 10)) == 0
#
#
# def test_sum3():
#     x = 0
#     assert sum((x, -10)) == -10

#
# @pytest.mark.parametrize(
#     ("n", "expected"),
#     [
#         (1, 2),
#         param(1, 0, marks=mark.xfail),
#         param(1, 3, marks=mark.xfail(reason="some bug")),
#         (2, 3),
#         (3, 4),
#         (4, 5),
#         # param(
#         #     0, 11, marks=mark.skipif(0, reason="0 not expected")
#         # ),
#     ],
# )
# def test_increment(n, expected):
#     assert sum((x,num)) == expected
