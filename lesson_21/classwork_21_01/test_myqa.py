import sys
import random
import some_mock
from unittest import TestCase, main, skip, skipIf, expectedFailure
from unittest.mock import MagicMock, patch

from employee import AutoQA, ManualQA, Manager
from some_mock import ProductionClass

def skipUnlessHasattr(obj, attr):
    if hasattr(obj, attr):
        return lambda func: func
    else:
        return skip("{!r} doesn't have {!r}".format(obj, attr))

def hello(*args):
    with open('temp.cfg' , 'w') as f:
        f.write("Done\n")
        f.writelines(str(args))
    return 100

class TestProduction(TestCase):
    def test_method_value_50(self):
        real = ProductionClass()
        real.some_method = MagicMock()
        real.some_method.return_value = 50
        value = real.method()
        self.assertEqual(50, value)

    def test_method_assertion(self):
        real = ProductionClass()
        real.some_method = MagicMock()
        real.some_method.return_value = -1
        with self.assertRaises(AssertionError):
            real.method()

    def test_method_some_method_assertion(self):
        real = ProductionClass()
        real.some_method = MagicMock()
        real.some_method.side_effect = hello
        real.method()
        real.method()
        real.method()
        print(real.some_method.call_count)

    @patch('some_mock.ProductionClass.some_method')
    def test_method_some_method_assertion(self, some_method):
        real = some_mock.ProductionClass()
        real.some_method.return_value = 50
        real.method()
        real.method()
        print(real.some_method.call_count)


    def test_method_range(self):
        real = ProductionClass()
        boolvalue = 1 < real.method() < 10000
        self.assertTrue(boolvalue)


class TestAutoQA(TestCase):
    #@skip("Skip JIRABUGID Niv Simon")
    @expectedFailure
    def test_doc(self):
        expected_result = True
        qa = AutoQA('Sergii')
        result = qa.test_doc('session13_plan.txt')  # True or False
        self.assertEqual(expected_result, bool(result))


class TestManualQA(TestCase):
    def test_mq_none_doc_result(self):
        qa = ManualQA('Sasha')
        result = qa.test_doc('session13_plan.txt')  # True or False
        self.assertFalse(result)


class TestManager(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.mgr = Manager()
        cls.man_qa = ManualQA('Anna')
        cls.auto_qa = AutoQA("Tim")
        cls.qa = random.sample([AutoQA('Sergii'), cls.auto_qa, cls.man_qa], 1)[0]

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.mgr
        del cls.qa

    def setUp(self) -> None:
        print("\nStart testing in the TestManager class")

    def tearDown(self) -> None:
        print("Tested TestManager class")

    @skipUnlessHasattr(AutoQA("Anna"), '_name')
    def test_doc(self):
        result = self.mgr.release(self.auto_qa)  # True or False
        self.assertEqual(True, bool(result))

    @skipIf(sys.platform == 'darwin', "Skipped for the windows hosts")  # darwin, linux
    def test_mgr_release(self):
        result = self.mgr.release(self.qa)  # True or False
        self.assertEqual(True, bool(result))


if __name__ == "__main__":
    main()
