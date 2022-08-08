# One more module for testing
import requests
import random
import abc


class QA(abc.ABC):
    @abc.abstractmethod
    def test_doc(self, path):
        # instruction to test some doc path
        if all(['ms1', 'ms2', 'ms3']):
            _pass = True
        else:
            _pass = False
        return _pass


class ManualQA(QA):
    def __init__(self, name):
        self.name = name

    def test_doc(self, path):
        super().test_doc(path)


class AutoQA(QA):
    def __init__(self, name):
        self.name = name

    def test_doc(self, path):
        _pass = False
        try:
            with open(path) as f:
                f.read()
                _pass = True
        except IOError:
            print("Failed to read file")
        return _pass


class Manager:
    def release(self, QA):
        return QA.test_doc("session13_plan.txt")


mgr = Manager()
ga = random.sample([AutoQA('Sergii'), AutoQA('Sasha'), ManualQA('Anna')], 1)
mgr.release(ga[-1])


class Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return "{}.{}@email.com.ua".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def weekly_report(self, week):
        response = requests.get('http://company/com/{0}/reports/{1}'.format(self.first, week))
        # Test result will depend on site respond
        if response.ok:
            return response.text
        else:
            return "No response!"
