import requests
from datetime import datetime


class LinkAnalyzer:
    def __init__(self, dict_url):
        self.dict_url = dict_url
        self.list_links = []
        self.invalid_links = []
        self.valid_links = []

    def collect_links(self):
        for link in self.dict_url['url']:
            self.list_links.append(link)
        return self.list_links

    def review_link(self, link=None):
        try:
            requests.get(link)
            return True
        except requests.RequestException:
            return False

    def review_links(self, links=None):
        for link in links:
            try:
                requests.get(link)
                self.valid_links.append(link)
            except requests.RequestException:
                self.invalid_links.append(link)

    def clean(self):
        self.list_links = []
        self.invalid_links = []

    def make_report(self):
        now = datetime.now()
        with open("report_date_time_number_of_links.txt", "w") as f:
            data_time = now.strftime("%m/%d/%Y, %H:%M:%S")
            f.write(
                f"{data_time}\nLinks {self.list_links}\nValid {self.valid_links}\nInvalid {self.invalid_links}")
