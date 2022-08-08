"""
Задача 1. Використовуючи unittest, створити тести, що будуть перевіряти наявність відповідних імен зі списку очікуваних.
Задача 2. Створити тести, що перевіряють відповідність значень ключів: domain, secure, version, expires (timestamp)
Задача 3. Новий кукі 'MNC' в розробці та очікується під час релізу. Необхідно створити тести для ще неіснуючого кукі з
задач 1 та 2 використовуючи мок. (Можна використати with patch.dict)
"""
from datetime import datetime, timedelta
from unittest import TestCase, main
from unittest.mock import patch
from youtube_cookies import get_cookies

URL = "https://www.youtube.com/"

LIST_KEY_COOKIES = ['GPS', 'YSC', 'VISITOR_INFO1_LIVE']
ACTUAL_RESULT = get_cookies(URL)
DICT_KEYS = {
    'domain': '.youtube.com',
    'secure': True,
    'version': 0,
    'expires': (datetime.now() + timedelta(minutes=30)).strftime('%Y-%m-%d %H:%M:%S')
}


class TestYoutubeCookieNames(TestCase):
    """Test YouTube cookies with names from the list"""

    def test_youtube_cookie_name_GPS(self):
        expected_result = LIST_KEY_COOKIES[0]
        actual_result = get_cookies(URL)

        self.assertTrue(expected_result in actual_result)

    def test_youtube_cookie_name_YSC(self):
        expected_result = LIST_KEY_COOKIES[1]
        actual_result = get_cookies(URL)

        self.assertTrue(expected_result in actual_result)

    def test_youtube_cookie_name_VISITOR_INFO1_LIVE(self):
        expected_result = LIST_KEY_COOKIES[2]
        actual_result = get_cookies(URL)

        self.assertTrue(expected_result in actual_result)


class TestYoutubeCookiesValues(TestCase):
    """Test YouTube cookies contain values"""

    def test_youtube_cookie_name_GPS_contain_domain_value(self):
        expected_result = DICT_KEYS['domain']
        actual_result = get_cookies(URL)['GPS'].domain

        self.assertEqual(expected_result, actual_result)

    def test_youtube_cookie_name_GPS_contain_secure_value(self):
        expected_result = DICT_KEYS['secure']
        actual_result = get_cookies(URL)['GPS'].secure

        self.assertEqual(expected_result, actual_result)

    def test_youtube_cookie_name_GPS_contain_version_value(self):
        expected_result = DICT_KEYS['version']
        actual_result = get_cookies(URL)['GPS'].version

        self.assertEqual(expected_result, actual_result)

    def test_youtube_cookie_name_GPS_contain_expires_value(self):
        expected_result = DICT_KEYS['expires']
        actual_result = datetime.fromtimestamp(int(ACTUAL_RESULT['GPS'].expires)).strftime('%Y-%m-%d %H:%M:%S')

        self.assertEqual(expected_result[:-3], actual_result[:-3])

    def test_youtube_cookie_name_YSC_contain_domain_value(self):
        expected_result = DICT_KEYS['domain']
        actual_result = get_cookies(URL)['YSC'].domain

        self.assertEqual(expected_result, actual_result)

    def test_youtube_cookie_name_YSC_contain_secure_value(self):
        expected_result = DICT_KEYS['secure']
        actual_result = get_cookies(URL)['YSC'].secure

        self.assertEqual(expected_result, actual_result)

    def test_youtube_cookie_name_YSC_contain_version_value(self):
        expected_result = DICT_KEYS['version']
        actual_result = get_cookies(URL)['YSC'].version

        self.assertEqual(expected_result, actual_result)

    def test_youtube_cookie_name_YSC_contain_expires_value(self):
        expected_result = None
        actual_result = get_cookies(URL)['YSC'].expires

        self.assertEqual(expected_result, actual_result)

    def test_youtube_cookie_name_VISITOR_INFO1_LIVE_contain_domain_value(self):
        expected_result = DICT_KEYS['domain']
        actual_result = get_cookies(URL)['VISITOR_INFO1_LIVE'].domain

        self.assertEqual(expected_result, actual_result)

    def test_youtube_cookie_name_VISITOR_INFO1_LIVE_contain_secure_value(self):
        expected_result = DICT_KEYS['secure']
        actual_result = get_cookies(URL)['VISITOR_INFO1_LIVE'].secure

        self.assertEqual(expected_result, actual_result)

    def test_youtube_cookie_name_VISITOR_INFO1_LIVE_contain_version_value(self):
        expected_result = DICT_KEYS['version']
        actual_result = get_cookies(URL)['VISITOR_INFO1_LIVE'].version

        self.assertEqual(expected_result, actual_result)

    def test_youtube_cookie_name_VISITOR_INFO1_LIVE_contain_expires_value(self):
        expected_result = (datetime.now() + timedelta(days=180) - timedelta(hours=1) - timedelta(seconds=4)).strftime(
            '%Y-%m-%d %H:%M:%S')
        actual_result = datetime.fromtimestamp(int(ACTUAL_RESULT[
                                                       'VISITOR_INFO1_LIVE'].expires)).strftime('%Y-%m-%d %H:%M:%S')

        self.assertEqual(expected_result[:-3], actual_result[:-3])


class TestYoutubeNewCookie(TestCase):
    """Test YouTube cookies contain mock"""

    def setUp(self) -> None:
        self.dict_mock_keys = {
            'domain': '.youtube.com',
            'secure': True,
            'version': 0,
            'expires': (datetime.now() + timedelta(minutes=30)).strftime('%Y-%m-%d %H:%M:%S')
        }

    @patch('youtube_cookies.get_cookies', return_value='MNC')
    def test_youtube_cookie_name_MNC(self, get_cookies):
        expected_result = 'MNC'

        self.assertTrue(expected_result in get_cookies(URL))

    @patch('youtube_cookies.get_cookies', return_value='.youtube.com')
    def test_youtube_cookie_name_MNC_contain_domain_value(self, get_cookies):
        expected_result = self.dict_mock_keys['domain']

        self.assertEqual(expected_result, get_cookies(URL))

    @patch('youtube_cookies.get_cookies', return_value=True)
    def test_youtube_cookie_name_MNC_contain_secure_value(self, get_cookies):
        expected_result = self.dict_mock_keys['secure']

        self.assertEqual(expected_result, get_cookies(URL))

    @patch('youtube_cookies.get_cookies', return_value=0)
    def test_youtube_cookie_name_MNC_contain_version_value(self, get_cookies):
        expected_result = self.dict_mock_keys['version']

        self.assertEqual(expected_result, get_cookies(URL))

    @patch('youtube_cookies.get_cookies',
           return_value=(datetime.now() + timedelta(minutes=30)).strftime('%Y-%m-%d %H:%M:%S'))
    def test_youtube_cookie_name_MNC_contain_expires_value(self, get_cookies):
        expected_result = self.dict_mock_keys['expires']

        self.assertEqual(expected_result[:-3], get_cookies(URL)[:-3])


if __name__ == '__main__':
    main()
