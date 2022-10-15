#  pip install -r requirements.txt

# Set additional argument
# -p no:cacheprovider --alluredir=/tmp/reports/allure-results
# -p no:cacheprovider --html=/tmp/reports/htmls/report.html
# -p no:cacheprovider --reruns 3   # pip install pytest-rerunfailures


# Known issues
Если возникло "ImportError: cannot import name 'MarkInfo'"
	То удалить pytest-selenium

Если нет модуля allure: 'pip install allure-pytest'

Если возникло "ModuleNotFoundError: No module named 'webdriver_manager'"
	То 'pip install webdriver-manager' 

Если "TypeError: __init__() missing 3 required positional arguments: 'excinfo', 'start', and 'stop'"
	То обновить flaky в pip до последней версии

# To run tests
* clone the project 
```git clone```
* open the project in PyCharm
* [configure PyCharm to use pytest as default test runner](https://stackoverflow.com/a/6397315/1562282)
* click on green triangle near test that you want to run

# HTML Report
![Alt text](doc/html.png?raw=true "HTML Report")
# Allure Report
http://biercoff.com/opening-local-version-of-allure-report-with-chrome/
![Alt text](doc/allure.png?raw=true "Allure Report")
# Re-run failed tests
![Alt text](doc/re-run.png?raw=true "Re-run Failed")
