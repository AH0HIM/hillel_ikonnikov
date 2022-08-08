import requests


def get_cookies(url):
    response = requests.get(url)
    cookies_dict = response.cookies._cookies
    return cookies_dict['.youtube.com']['/']
