import requests


URL = "https://www.youtube.com/"


def get_cookies(url):
    response = requests.get(url)
    cookies_dict = response.cookies._cookies
    return cookies_dict['.youtube.com']['/']


if __name__ == '__main__':
    print(get_cookies(URL))


def sum_2(a, b):
    return a + b
