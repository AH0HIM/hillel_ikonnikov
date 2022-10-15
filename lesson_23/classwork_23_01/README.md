# pip install -r requirements.txt

# Set additional argument
# -p no:cacheprovider --alluredir=/tmp/reports/allure-results
# -p no:cacheprovider --html=/tmp/reports/htmls/reports. html
# -p no:cacheprovider --reruns 3

# Known issues
Если возникло "ImportError: cannot import name 'MarkInfo'"
    То удалить pytest-selenium

Если нет модуля allure: 'pip install allure-pytest'

Если возникло "ModuleNotFountError: No module named 'webdriver_manager'"
    То 'pip install webdriver-manager'

Если "TypeError: __init__() missing 3 required position arguments: 'excinfo', 'start', and 'stop'"
    То обновить flaky в pip до последней версии

# To run tests
* close the project