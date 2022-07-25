import requests


class LinkAnalyzer:
    LINK_TYPES = ['url', 'link', 'http']

    def __init__(self):
        self.text = "text"
        self.verified_links = []

    def check_link(self, raw_link):
        respond = requests.get(raw_link.strip())
        return respond.ok

    def check_links(self, links):
        for link in links:
            assert self.check_link(link), "Broken link"

    def link_data(self, raw_link):
        respond = requests.get(raw_link.strip())
        json_data = respond.json() if respond.ok else {}
        return json_data
