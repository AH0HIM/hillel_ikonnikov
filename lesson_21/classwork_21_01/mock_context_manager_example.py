import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    def test_weekly_report(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            report = Employee('Sergii', 'T', 1).weekly_report('W40')
            mocked_get.assert_called_with('http://company/com/Sergii/reports/W40')
            self.assertEqual(report, "Success")
            print(mocked_get.called, mocked_get.call_count)

            mocked_get.return_value.ok = False

            report = Employee('S', 'T', 1).weekly_report('W52')
            mocked_get.assert_called_with('http://company/com/S/reports/W52')
            self.assertEqual(report, "No response!")


if __name__ == "__main__":
    unittest.main()