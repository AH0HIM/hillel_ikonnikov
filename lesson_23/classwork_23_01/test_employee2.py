import time

from unittest import skip
from pytest import mark
from .employee import Employee

class TestPerson:
    def test_email(self):
        emp1 = Employee('Sergii', 'T', 5000)
        assert "sergii.t@email.com.ua" == emp1.email
        print("Test Pass")


    @mark.xfail(reason="Because", run=False)   #  1 failed, 5 passed, 1 xfailed, 1 warning in 0.67s
    #@skip                            # 1 failed, 6 passed, 1 warning in 0.66s
    def test_email2(self):
        emp1 = Employee('Sergi', 'T', 5000)
        # pdb.set_trace()
        time.sleep(10)
        assert "sergii.t@email.com.ua" == emp1.email
        print("Test Pass")


@mark.ui
@mark.smoke
@mark.regression("SSENG-20458")
def test_apply_raise():
    emp1 = Employee('Sergii', 'T', 5000)
    emp1.apply_raise()
    assert emp1.pay == 5000 * 1.05
    print("Test Pass")
